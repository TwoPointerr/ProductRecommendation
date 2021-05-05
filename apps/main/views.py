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
# Create your views here.



def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    allcat = Category.objects.all()
    productcount = request.session.get('productcount')
    return render(request, "home-fashion-store-v2.html", {'product_list': product_list, 'allcat': allcat, 'productcount':productcount})

def show_all_products(request):
    product_list = Product.objects.all()
    minprice = Product.objects.all().aggregate(Min('market_price'))['market_price__min']
    maxprice = Product.objects.all().aggregate(Max('market_price'))['market_price__max']
    subCategory_list = ['Topwear', 'Bottomwear', 'Dress', 'Saree', 'Shoes', 'Innerwear', 'Headwear', 'Socks', 'Flip Flops']
    all_articel_type_list = ['Belts', 'Blazers', 'Booties', 'Boxers', 'Bra', 'Briefs', 'Camisoles', 'Capris', 'Caps', 'Casual Shoes', 'Churidar', 'Dresses', 'Dupatta', 'Flats', 'Flip Flops', 'Formal Shoes', 'Hat', 'Headband', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jeggings', 'Jumpsuit', 'Kurtas', 'Kurtis', 'Leggings', 'Lehenga Choli', 'Nehru Jackets', 'Patiala', 'Rain Jacket', 'Rain Trousers', 'Rompers', 'Salwar', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shapewear', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Socks', 'Sports Shoes', 'Stockings', 'Suits', 'Suspenders', 'Sweaters', 'Sweatshirts', 'Swimwear', 'Tights', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Trunk', 'Tshirts', 'Tunics', 'Waistcoat']
    all_category = Category.objects.all()
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    return render(request, "shop-grid-ls.html", {'product_list': product_list, 'all_category': all_category,'sub_category':subCategory_list,'article_type':all_articel_type_list, 'minprice':minprice, 'maxprice':maxprice})

def category(request):
    allcat = Category.objects.all()
    productcount = request.session.get('productcount')
    return render(request, "home-fashion-store-v2.html", {'allcat': allcat, 'productcount':productcount})


def productdetail(request, slug):
    url_slug = slug
    product = Product.objects.get(slug=url_slug)
    return render(request, "shop-single-v2.html", {'product': product})

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
    categories= request.GET.getlist('category[]')
    product_list = Product.objects.all().order_by('-id')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    product_list = product_list.filter(market_price__gte=min_price).order_by('market_price')
    product_list = product_list.filter(market_price__lte=max_price).order_by('market_price')
    if len(categories)>0:
        category = Category.objects.filter(title__in=categories)
        cat_id = []
        for cat in category:
            cat_id.append(cat.id)
        product_list = product_list.filter(category__in=cat_id)
    template = render_to_string('ajax/product-list.html', {'product_list': product_list})
    return JsonResponse({'data':template})