
from django.contrib import admin
from django.urls import path
from apps.main import views

urlpatterns = [
    path('',views.index, name="index"),
    path('category/',views.category, name="category"),
    path('product/<slug:slug>/',views.productdetail, name="productdetail"),
    path('addtocart-<int:pid>/',views.addtocart, name="addtocart"),
    path('my-cart/',views.mycart, name="mycart"),
    path('checkout/detail',views.checkout_detail,name='checkout_detail'),
    path('checkout/review',views.checkout_review,name='checkout_review'),
    path('checkout/payment',views.checkout_payment,name='checkout_payment')
]
