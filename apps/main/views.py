from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

def index(request):
    product_list = Product.objects.all()
    return render(request, "shop-grid-ft.html", {'product_list':product_list})

def category(request):
    allcat = Category.objects.all()
    return render(request, "home-fashion-store-v2.html", {'allcat':allcat})

def productdetail(request, slug):
    url_slug=slug
    product = Product.objects.get(slug=url_slug)
    return render(request, "shop-single-v2.html", {'product':product})

def addtocart(request, pid):
    url_pid=pid
    product_obj = Product.objects.get(id=url_pid)

    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart_obj = Cart.objects.get(id=cart_id)
        this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
        if this_product_in_cart.exists():
            cartproduct = this_product_in_cart.last()
            cartproduct.quantity +=1
            cartproduct.subtotal += product_obj.market_price
            cartproduct.save()
            cart_obj.total +=product_obj.market_price
            cart_obj.save()
        else:
            cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1,
            subtotal=product_obj.market_price)
            cart_obj.total += product_obj.market_price
            cart_obj.save


        
    else:
        cart_obj = Cart.objects.create(total=0)
        request.session['cart_id'] = cart_obj.id
        cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.market_price, quantity=1, subtotal=product_obj.market_price)
        cart_obj.total += product_obj.market_price
        cart_obj.save

    return render(request, "shop-cart.html", {'product_obj':product_obj})

















"""     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        context['allcategories'] = Category.objects.all() 
        return context """  