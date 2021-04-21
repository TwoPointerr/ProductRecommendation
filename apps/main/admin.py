from django.contrib import admin
from .models import Customer, Cart, CartProduct, Category, Order, Product


admin.site.register([Customer, Cart, CartProduct, Category, Order, Product])
# Register your models here.
