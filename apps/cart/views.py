from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from apps.cart.models import *

# Create your views here.

def addtocart(request, pid):
    url_pid = pid
    product_obj = Product.objects.get(id=url_pid)

    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        this_product_in_cart = cart_obj.cartproduct_set.filter(
            product=product_obj)
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
            

    else:
        
        cart_obj = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_obj.id
        cartproduct = CartProduct.objects.create(
            cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
        cart_obj.total += product_obj.market_price
        
        cart_obj.save()
        
    #return render(request, "proadded.html")
    return redirect('apps.cart:mycart')


def mycart(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        print(cart.total)
    else:
        cart = None
        
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

        else:
            pass
        return redirect('apps.cart:mycart')