from django.contrib import admin
from .models import Cart, CartProduct, Order, Product


admin.site.register([Cart, CartProduct, Order, Product])
# Register your models here.
