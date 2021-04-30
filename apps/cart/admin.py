from django.contrib import admin
from .models import Cart, CartProduct, Category, Order, Product


admin.site.register([Cart, CartProduct, Category, Order, Product])
# Register your models here.
