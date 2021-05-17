from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Count, Min, Sum, Avg, Max
from django.db.models import Q
from django.template.loader import render_to_string
from apps.cart.models import *

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from active_page import set_page_active

# Create your views here.

def index(request):
    set_page_active('Home')
    product_list = Product.objects.all()
    # paginator = Paginator(product_list, 2)
    # page_number = request.GET.get('page')
    # product_list = paginator.get_page(page_number)
    # allcat = Category.objects.all()
    return render(request, "home-fashion-store-v2.html", {'product_list': product_list})

def show_all_products(request):
    set_page_active('Shop')
    product_list = Product.objects.all().order_by('id')
    minprice = Product.objects.all().aggregate(Min('market_price'))['market_price__min']
    maxprice = Product.objects.all().aggregate(Max('market_price'))['market_price__max']
    subCategory_list = ['Topwear', 'Bottomwear', 'Dress', 'Saree', 'Shoes', 'Innerwear', 'Headwear', 'Socks', 'Flip Flops']
    all_articel_type_list = ['Belts', 'Blazers', 'Booties', 'Boxers', 'Bra', 'Briefs', 'Camisoles', 'Capris', 'Caps', 'Casual Shoes', 'Churidar', 'Dresses', 'Dupatta', 'Flats', 'Flip Flops', 'Formal Shoes', 'Hat', 'Headband', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jeggings', 'Jumpsuit', 'Kurtas', 'Kurtis', 'Leggings', 'Lehenga Choli', 'Nehru Jackets', 'Patiala', 'Rain Jacket', 'Rain Trousers', 'Rompers', 'Salwar', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shapewear', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Socks', 'Sports Shoes', 'Stockings', 'Suits', 'Suspenders', 'Sweaters', 'Sweatshirts', 'Swimwear', 'Tights', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Trunk', 'Tshirts', 'Tunics', 'Waistcoat']
    # all_category = Category.objects.all()
    gender_cat = Product.objects.values_list('gender_cat',flat=True).distinct()
    sub_cat = Product.objects.values_list('sub_cat',flat=True).distinct()
    articel_type = Product.objects.values_list('articel_type',flat=True).distinct()
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request, "shop-grid-ls.html", {'product_list': product_list,'gender_cat':list(gender_cat),'sub_category':list(sub_cat),'article_type':list(articel_type), 'minprice':minprice, 'maxprice':maxprice})

def category(request):
    # allcat = Category.objects.all()
    productcount = request.session.get('productcount')
    return render(request, "home-fashion-store-v2.html", {'productcount':productcount})




def Search_Result(request, keyword):

    search_result = Product.objects.filter(Q(title__icontains = keyword) | Q(description__icontains = keyword))
    paginator = Paginator(search_result, 2)
    page_number = request.GET.get('page')
    search_result = paginator.get_page(page_number)
    print(keyword, search_result)
    return render(request, 'search_result.html', {'keyword':keyword, 'search_result': search_result})

def Search_Product(request):
    product_list = Product.objects.all()
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        # return redirect('search_result'+ keyword)
        return HttpResponseRedirect(reverse('apps.main:search_result', args=[keyword]))

def Single_Product(request, pid):
   single_product = Product.objects.get(id = pid)
   return render(request, 'shop-single-v2.html', {'single_product':single_product}) 

#To Filter Data

def filter_data(request):
    gender_categories= request.GET.getlist('gender_category[]')
    sub_categories= request.GET.getlist('sub_category[]')
    article_categories= request.GET.getlist('article_category[]')
    sort_by_categories= request.GET.getlist('sort_by[]')
    color_filter= request.GET.getlist('color_filter[]')
    
    product_list = Product.objects.all().order_by('id')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    product_list = product_list.filter(market_price__gte=min_price).order_by('market_price')
    product_list = product_list.filter(market_price__lte=max_price).order_by('market_price')
    # product_sort_list = product_sort_list.all().order_by('title')
    if len(gender_categories)>0:
        # category = Category.objects.filter(title__in=categories)
        product_list = product_list.filter(gender_cat__in=gender_categories)
    if len(sub_categories)>0:
        product_list = product_list.filter(sub_cat__in=sub_categories)
    if len(article_categories)>0:
        product_list = product_list.filter(articel_type__in=article_categories)
    if len(sort_by_categories)>0:
        if(sort_by_categories[0] == 'l_h_sort_by'):
            product_list = product_list.all().order_by('market_price')
        elif(sort_by_categories[0] == 'h_l_sort_by'):
            product_list = product_list.all().order_by('-market_price')
        elif(sort_by_categories[0] == 'a_z_sort_by'):
            product_list = product_list.all().order_by('title')
        elif(sort_by_categories[0] == 'z_a_sort_by'):
            product_list = product_list.all().order_by('-title')
        # product_list = product_list.all().order_by('title')
    # prod_list = product_list
    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    
    template = render_to_string('ajax/product-list.html', {'product_list': product_list})
    return JsonResponse({'data':template})
