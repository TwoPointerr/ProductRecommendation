from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.


def index(request):
    product_list = Product.objects.all()
    return render(request, "shop-grid-ft.html", {'product_list': product_list})


def category(request):
    allcat = Category.objects.all()
    return render(request, "home-fashion-store-v2.html", {'allcat': allcat})


def productdetail(request, slug):
    url_slug = slug
    product = Product.objects.get(slug=url_slug)
    return render(request, "shop-single-v2.html", {'product': product})


def addtocart(request, pid):
    url_pid = pid
    product_obj = Product.objects.get(id=url_pid)

    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        this_product_in_cart = cart_obj.cartproduct_set.filter(
            product=product_obj)
        print("if 11:" + str(cart_obj.total))
        if this_product_in_cart.exists():
            print("if 21:" + str(cart_obj.total))
            cartproduct = this_product_in_cart.last()
            cartproduct.quantity += 1
            cartproduct.subtotal += product_obj.market_price
            cartproduct.save()
            cart_obj.total += product_obj.market_price
            cart_obj.save()
            print("if 22:" + str(cart_obj.total))

        else:
            print("else11:" + str(cart_obj.total))
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
            cart_obj.total += product_obj.market_price
            """ print(cart_obj.total) """
            cart_obj.save()
            print("else 12: " + str(cart_obj.total))

    else:
        #print("else 21:" + str(cart_obj.total))
        cart_obj = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_obj.id
        cartproduct = CartProduct.objects.create(
            cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
        cart_obj.total += product_obj.market_price
        """ print(str(cart_obj.total)) """
        cart_obj.save()
        print("else 22:" + str(cart_obj.total))
    return render(request, "proadded.html")


def mycart(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        print(cart.total)
    else:
        cart = None
    return render(request, "shop-cart.html", {'cart': cart})

def checkout_detail(request):
    return render(request,"checkout-details.html")

def checkout_payment(request):
    return render(request,"checkout-payment.html")

def checkout_review(request):
    return render(request,"checkout-review.html")




