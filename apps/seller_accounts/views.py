from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from apps.cart.models import *
from apps.seller_accounts.models import *
from django.contrib import messages

from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from apps.seller_accounts.product_cat_ML import get_product_cat 
from django.conf import settings
import os
import pandas as pd

# Create your views here.

def signup(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password, is_staff=True)
        
        user.save()
        login(request, user)
        return redirect("apps.seller_accounts:company_details")
    return render(request, "seller_account_signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username= email, password= password)
        user = auth.authenticate(username = username, password = password)
        print(user)
        if user is not None:
            if user.is_staff:
                login(request, user)
                print("logged in")
                return redirect("apps.seller_accounts:profile")
            else:
                print("user is not staff")
            
        else:
            print("not logged in")
    return render(request, "seller_account_signin.html")

@login_required
def signout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully.')
    return redirect("apps.main:index")

@login_required
def profile(request):
    if check_is_seller(request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            print(firstname, lastname, username, email)
            user = User.objects.create_user(id=user_id, first_name=firstname, last_name=lastname, username=username, email=email, is_staff=True)
            user.save()
            login(request, user)
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "seller_account_profile.html", {'seller_user':user})

@login_required
def company_details(request):
    if check_is_seller(request):
        if request.method == 'POST':
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            companyname = request.POST.get('companyname')
            companyemail = request.POST.get('companyemail')
            company_desc = request.POST.get('description')
            companynumber = request.POST.get('companynumber')
            companydetail = CompanyDetails.objects.get_or_create(user=user, company_name=companyname, company_email=companyemail, company_desc=company_desc, company_number=companynumber)
            return redirect("apps.seller_accounts:address_info")
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "seller_account_company_detail.html")

@login_required
def address_info(request):
    if check_is_seller(request):
        if request.method == 'POST':
            user_id = request.user.id
            company = CompanyDetails.objects.get(user_id=user_id)
            addline = request.POST.get('Address')
            country = request.POST.get('Country')
            state = request.POST.get('State')
            city = request.POST.get('City')
            pincode = request.POST.get('Pincode')
            addressinfo = CompanyAddress.objects.get_or_create(company=company, addline=addline, country=country, state=state, city=city, pincode=pincode)
            return redirect("apps.seller_accounts:profile")
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "seller_account_address_info.html")

@login_required
def addnewproduct(request):
    if check_is_seller(request):
        return render(request, "dashboard-add-new-product.html")
    else:
        return redirect('apps.seller_accounts:signin')
        
@login_required
def add_single_product(request):
    if check_is_seller(request):
        if request.method == 'POST':
            product_name = request.POST.get("product_name")
            product_desc = request.POST.get("product_desc")
            product_img_urls = request.POST.get("product_img_urls")
            product_price = request.POST.get("product_price")
            product_img = request.FILES.getlist("product_img")
            product_cat = get_product_cat(product_name)
            product = Product.objects.create(title=product_name,
                                            gender_cat=product_cat['gender'],
                                            sub_cat=product_cat['sub_cat'],
                                            articel_type=product_cat['articel_type'],
                                            market_price=product_price,
                                            description=product_desc,
                                            seller=CompanyDetails.objects.get(user=request.user))
            upload_multiple_product_img(product,product_img,product_img_urls)
            sale=Sales.objects.create(company=CompanyDetails.objects.get(user=request.user),product=product, rate= product_price)
            messages.success(request,'Product Added Succesfully')
            print(product_name)
            print(product_cat['gender'],product_cat['sub_cat'],product_cat['articel_type'])
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "dashboard-add-new-product.html")

@login_required
def add_multiple_products(request):
    if check_is_seller(request):
        columns = ["product_name","product_desc","product_price","product_img_url"]
        if request.method == 'POST':
            products_file = request.FILES.get("multi_product_file")
            if products_file is not None:
                upload_file_to_media(products_file)
                full_file_path = get_file_path(settings.MEDIA_ROOT,products_file.name)
                df = pd.read_csv(full_file_path)
                seller = CompanyDetails.objects.get(user=request.user)
                for i in range(df.shape[0]):
                    product_cat = get_product_cat(df['product_name'][i])
                    product = Product.objects.create(title=df['product_name'][i],
                                                gender_cat=product_cat['gender'],
                                                sub_cat=product_cat['sub_cat'],
                                                articel_type=product_cat['articel_type'],
                                                image_url=df['product_img_url'][i],
                                                market_price=df['product_price'][i],
                                                description=df['product_desc'][i],
                                                seller=seller)
                    print("Product successfully added :",i,product.title)
            else:
                print("file is not uploaded")
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "dashboard-add-new-product.html")


@login_required
def editproduct(request, proid):
    if request.user.is_staff:
        seller = CompanyDetails.objects.get(user=request.user)
        product = Product.objects.filter(id=proid, seller=seller).last()
        product_img_urls = ProductImagesURL.objects.filter(product=product).order_by("id")
        if product :    
            previmg=product.image_file
            if request.method == 'POST':
                product.title = request.POST.get("product_name")
                product.description = request.POST.get("product_desc")
                product.market_price = request.POST.get("product_price")
                product.gender_cat=request.POST.get("product_gcat")
                product.sub_cat=request.POST.get("product_scat")
                product.articel_type=request.POST.get("product_atype")
                newimg=product.image_file
                if str(newimg) == '':
                    product.image_file = previmg
                # product.save(update_fields=['title','gender_cat', 'sub_cat', 'articel_type', 'market_price', 'description'])
                
                image_files = request.FILES.get("product_img")
                
                img_url_1 = request.POST.get("product_img_1_url")
                img_url_2 = request.POST.get("product_img_2_url")
                img_url_3 = request.POST.get("product_img_3_url")
                no_pro_img_urls = len(product_img_urls)
                if img_url_1 != "":
                    if no_pro_img_urls >= 1:
                        product_img_urls[0].image_url = img_url_1
                    else:
                        ProductImagesURL.objects.create(product=product,image_url=img_url_1)
                if img_url_2 != "":
                    if no_pro_img_urls >= 2:
                        product_img_urls[1].image_url = img_url_2
                    else:
                        ProductImagesURL.objects.create(product=product,image_url=img_url_2)
                if img_url_3 != "":
                    if no_pro_img_urls >= 3:
                        product_img_urls[2].image_url = img_url_3
                    else:
                        ProductImagesURL.objects.create(product=product,image_url=img_url_3)
                # messages.success(request,'Product updated.')
                # return redirect("apps.seller_accounts:companyproducts")
        else:
            messages.warning(request,'Product not found.')
            return redirect("apps.seller_accounts:companyproducts")    
    else:
        messages.warning(request,'Login as Seller Account.')
        return redirect("apps.seller_accounts:signin")    
            
    return render(request, "dashboard-edit-product.html",{'product':product,'product_img_urls': product_img_urls})


@login_required
def deleteproduct(request, proid):
    if request.user.is_staff:
        seller = CompanyDetails.objects.get(user=request.user)
        product = Product.objects.filter(id=proid, seller=seller).last()
        
        if product :    
            product.delete()
            messages.warning(request,'Product deleted.')
            return redirect("apps.seller_accounts:companyproducts")
        else:
            messages.warning(request,'Product not found.')
            return redirect("apps.seller_accounts:companyproducts")    
    else:
        messages.warning(request,'Login as Seller Account.')
        return redirect("apps.main:index")    

    return render(request, "dashboard-edit-product.html",{'product':product})


@login_required
def companyinfo(request):
    if check_is_seller(request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        company_info = CompanyDetails.objects.get(user = user)
        addressinfo = CompanyAddress.objects.get(company = company_info)
        if request.method == 'POST':
            companyname = request.POST.get('companyname')
            companyemail = request.POST.get('companyemail')
            company_desc = request.POST.get('description')
            companynumber = request.POST.get('companynumber')
            addline = request.POST.get('Address')
            country = request.POST.get('Country')
            state = request.POST.get('State')
            city = request.POST.get('City')
            pincode = request.POST.get('Pincode')
            companydetail = CompanyDetails.objects.filter(id=company_info.id).update(company_name=companyname, company_email=companyemail, company_desc=company_desc, company_number=companynumber)
            addressinfo = CompanyAddress.objects.filter(id=addressinfo.id).update(addline=addline, country=country, state=state, city=city, pincode=pincode)
            return redirect("apps.seller_accounts:companyinfo")
    else:
        return redirect('apps.seller_accounts:signin')
    return render(request, "seller_account_company_info.html",{'company_info': company_info, 'address_info': addressinfo})

""" @login_required
def companysales(request):
    if check_is_seller(request):
        orders(request)
    else:
        return redirect('apps.seller_accounts:signin') """

@login_required
def companyproducts(request):
    if check_is_seller(request):
        seller = CompanyDetails.objects.get(user=request.user)
        sale = Sales.objects.filter(company=seller).order_by("-id")
        return render(request, "dashboard-products.html",{'sale':sale})
    else:
        return redirect('apps.seller_accounts:signin')

def get_file_path(base_url,filename):
    file_path = os.path.join(base_url, filename)   #full path to text.
    return file_path

def upload_file_to_media(filename):
    fs = FileSystemStorage()
    filename = fs.save(filename.name,filename)
    return fs.url(filename)

@login_required
def orders(request):
    if request.user.is_staff:
        seller = CompanyDetails.objects.get(user=request.user)
        sale = Sales.objects.filter(company=seller).order_by("-id")
        product = Product.objects.filter(seller=seller)
        cart= Cart.objects.filter(ordered='True')
        orders=[]
        # total=0
        for cart in cart:
            cartproduct = CartProduct.objects.filter(cart=cart)
            for cp in cartproduct:
                if (cp.product in product):
                    order= Order.objects.filter(cart=cart).last()
                    if order:
                        if (order in orders):
                            
                            for ord in orders:
                                if ord == order:
                                    ord.total+=cp.subtotal
                        else:
                            order.total=cp.subtotal
                            orders.append(order)
    return render(request, 'dashboard-payouts.html', {'orders': orders})



@login_required
def orderdetail(request, orderid):
    if request.user.is_authenticated and CompanyDetails.objects.filter(user=request.user).exists():
        order_id = orderid
        seller = CompanyDetails.objects.get(user=request.user)
        product = Product.objects.filter(seller=seller)
        cart= Cart.objects.filter(ordered='True')
        total=0
        for cart in cart:
            cartproduct = CartProduct.objects.filter(cart=cart)
            for cp in cartproduct:
                if (cp.product in product):
                    order= Order.objects.get(id=order_id)   
                    if cp.cart == order.cart:
                        total += cp.subtotal
        order.total = total

        if request.method == 'POST':
            status = request.POST.get('status')
            if order:
                order.order_status=status
                order.save(update_fields=['order_status'])

                      
    else:
        return redirect("apps.seller_accounts:signin")
    return render(request, 'dashboard-seller-order.html', {'order':order,'product':product})




    """ 
        total sell count
        seller = CompanyDetails.objects.get(user=request.user)

        product = Product.objects.filter(id=proid, seller=seller).last()
        totalsell=Sales.objects.filter(company=seller).aggregate(sum=Sum('subtotal'))
        total=totalsell['sum'] """

def check_is_seller(request):
    if not request.user.is_staff:
        messages.warning(request,'You are signed in as Customer')
        return False
    else:
        return True

def upload_multiple_product_img(product,product_img,product_img_urls):
    if product_img:
        for img_file in product_img:
            product_img_file = ProductImagesFiles.objects.create(product=product,image_file=img_file)

    elif product_img_urls:
        img_url_list = product_img_urls.split("|")
        for url in img_url_list:
            img_urls = ProductImagesURL.objects.create(product=product,image_url=url)
    else:
        print("No img")