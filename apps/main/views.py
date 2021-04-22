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

















"""     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        context['allcategories'] = Category.objects.all() 
        return context """  