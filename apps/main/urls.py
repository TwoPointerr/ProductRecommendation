
from django.contrib import admin
from django.urls import path
from apps.main import views

urlpatterns = [
    path('',views.index, name="index"),
    path('category/',views.category, name="category"),
    path('product/<slug:slug>/',views.productdetail, name="productdetail"),
    path('addtocart-<int:pid>/',views.addtocart, name="addtocart"),
    path('my-cart/',views.mycart, name="mycart")
]
