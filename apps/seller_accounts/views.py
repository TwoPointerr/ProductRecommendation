from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from apps.seller_accounts.models import *

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

def signout(request):
    pass

def profile(request):
    user_id = request.user.id
    if request.user.is_staff:
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
    
    return render(request, "seller_account_profile.html", {'seller_user':user})

def company_details(request):
    if request.method == 'POST':
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        companyname = request.POST.get('companyname')
        companyemail = request.POST.get('companyemail')
        company_desc = request.POST.get('description')
        companynumber = request.POST.get('companynumber')
        companydetail = CompanyDetails.objects.get_or_create(user=user, company_name=companyname, company_email=companyemail, company_desc=company_desc, company_number=companynumber)
        return redirect("apps.seller_accounts:address_info")
    return render(request, "seller_account_company_detail.html")

def address_info(request):
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
    return render(request, "seller_account_address_info.html")

def addnewproduct(request):
    return render(request, "dashboard-add-new-product.html")

def companyinfo(request):
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

    return render(request, "seller_account_company_info.html",{'company_info': company_info, 'address_info': addressinfo})

def companysales(request):
    return render(request, "dashboard-sales.html")

def companyproducts(request):
    return render(request, "dashboard-products.html")
