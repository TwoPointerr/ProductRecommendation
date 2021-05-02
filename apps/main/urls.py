
from django.contrib import admin
from django.urls import path
from apps.main import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "apps.main"
urlpatterns = [
    path('',views.index, name="index"),
    path('category/',views.category, name="category"),
    path('product/<slug:slug>/',views.productdetail, name="productdetail"),
    # path('addtocart-<int:pid>/',views.addtocart, name="addtocart"),
    # path('my-cart/',views.mycart, name="mycart"),
    path('checkout/detail',views.checkout_detail,name='checkout_detail'),
    path('checkout/review',views.checkout_review,name='checkout_review'),
    path('checkout/payment',views.checkout_payment,name='checkout_payment')
   

    path("search_result/<str:keyword>", views.Search_Result,  name = "search_result"),
    path("search/", views.Search_Product,  name = "search_product"),
    path("single_product/<int:pid>/", views.Single_Product,  name = "single_product"),
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)