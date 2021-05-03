from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from apps.cart.models import *

# Create your views here.
productcount=0
#productcount = CartProduct.objects.filter(cart=cart).count()
def addtocart(request, pid):
    url_pid = pid
    product_obj = Product.objects.get(id=url_pid)
    profile = Profile.objects.get(id=request.user.profile.id)
    #cart_id = request.session.get("cart_id", None)
    cart_obj= Cart.objects.filter(profile=profile, ordered='False').last()

    if cart_obj:
        cart_id=cart_obj.id
        cart_obj = Cart.objects.get(id=cart_id)
        this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)

        if this_product_in_cart.exists():
            cartproduct = this_product_in_cart.last()
            cartproduct.quantity += 1
            cartproduct.subtotal += product_obj.market_price
            cartproduct.save()
            cart_obj.total += product_obj.market_price
            cart_obj.save()
        
        else:
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
            cart_obj.total += product_obj.market_price
            cart_obj.save()
            productcount = CartProduct.objects.filter(cart=cart_obj).count()
            
    else:
        cart_obj = Cart.objects.create(total=0, profile=profile)
        #request.session['cart_id'] = cart_obj.id
        cartproduct = CartProduct.objects.create(
            cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
        cart_obj.total += product_obj.market_price
        cart_obj.save()
        
    
    #return render(request, "proadded.html")
    return redirect('apps.cart:mycart')


def mycart(request):
    
    profile = Profile.objects.get(id=request.user.profile.id)
    #cart_id = request.session.get("cart_id", None)
    cart= Cart.objects.filter(profile=profile, ordered='False').last()
    if cart:
        cart = Cart.objects.get(id=cart.id)        
            
    else:
        cart = Cart.objects.create(total=0, profile=profile)
    #productcount = request.session.get('productcount')    
    return render(request, 'shop-cart.html', {'cart': cart})


def managecart(request, cpid):
    
        cp_id = cpid
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart

        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()
                #productcount = CartProduct.objects.filter(cart=cart_obj).count()
                #print(productcount)
        else:
            pass
        return redirect('apps.cart:mycart')

def emptycart(request):
        profile = Profile.objects.get(id=request.user.profile.id)
        cart= Cart.objects.filter(profile=profile).last()
        if cart.id:
            cart = Cart.objects.get(id=cart.id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("apps.cart:mycart")



def checkoutdetails(request):
    user = request.user
    profile = Profile.objects.get(id=request.user.profile.id)
    address= Address.objects.filter(profile=profile,isprimary=True).last()
    # address_list= Address.objects.all().order_by('-id')
    cart = Cart.objects.filter(profile=profile, ordered='False').last()
    order = Order.objects.filter(cart=cart).last()
    if request.user.is_authenticated:
        if cart:
            print(cart)
            if request.method == 'POST':
                addr = request.POST.get('address')
                if addr == 'new':
                    addline = request.POST.get('addline')
                    city = request.POST.get('city')
                    state = request.POST.get('state')
                    pincode = request.POST.get('zipcode')
                    firstname = request.POST.get('firstname')
                    lastname = request.POST.get('lastname')
                    email = request.POST.get('emailadd')
                    mob_no = request.POST.get('phoneno')
                else:
                    addline = address.addline
                    city = address.city
                    state = address.state
                    pincode = address.pincode
                    firstname = user.first_name
                    lastname = user.last_name
                    email = user.email
                    mob_no = profile.mob_no

                ordered_by = firstname +" "+ lastname
                shipping_address = addline +" "+ city +" "+ state +" - "+ str(pincode)
                subtotal = cart.total
                total = subtotal
                order_status = "Order Processing"
                


                order, created = Order.objects.update_or_create(
                    cart_id=cart.id,
                    defaults={'ordered_by':ordered_by, 'shipping_address':shipping_address,'mob_no':mob_no,'email':email,'subtotal':subtotal, 'order_status':order_status, 'total':total},
                )
                # completing order here
                cart.ordered = True
                cart.save(update_fields=['ordered'])
                # print(cart.id)
                cart = Cart.objects.create(total=0, profile=profile)
                # print(cart.id)
        else:
            return redirect("apps.main:index")
         
    else:
        return redirect("apps.accounts:signin")

    return render(request, "checkout-details.html",{'profile': profile, 'address':address, 'order':order})