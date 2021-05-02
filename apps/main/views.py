from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from apps.cart.models import *
# Create your views here.


def index(request):
    product_list = Product.objects.all()
    print(product_list)
    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    allcat = Category.objects.all()
    return render(request, "home-fashion-store-v2.html", {'product_list': product_list, 'allcat': allcat})


def category(request):
    allcat = Category.objects.all()
    print(allcat)
    return render(request, "home-fashion-store-v2.html", {'allcat': allcat})


def productdetail(request, slug):
    url_slug = slug
    product = Product.objects.get(slug=url_slug)
    return render(request, "shop-single-v2.html", {'product': product})

def Search_Result(request, keyword):

    search_result = Product.objects.filter(title__icontains = keyword)
    return render(request, 'search.html', {'keyword':keyword, 'search_result': search_result})

def Search_Product(request):
    product_list = Product.objects.all()
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        # return redirect('search_result'+ keyword)
        return HttpResponseRedirect(reverse('apps.main:search_result', args=[keyword]))

def Single_Product(request, pid):
   single_product = Product.objects.get(id = pid)
   return render(request, 'shop-single-v2.html', {'single_product':single_product}) 

