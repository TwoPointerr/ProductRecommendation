from django.contrib import admin
from .models import Sales, Cart, CartProduct, Order, Product


admin.site.register([Sales, Cart, CartProduct, Order, Product])
# Register your models here.
