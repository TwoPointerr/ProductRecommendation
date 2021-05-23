from django.db import models
from django.db.models.deletion import CASCADE
from apps.accounts.models import *
from django.contrib.auth.models import User
from apps.seller_accounts.models import *
from django.core.files import File
import os
import urllib.request
# Create your models here.

# class Category(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    gender_cat = models.CharField(max_length=50,null=True)
    sub_cat = models.CharField(max_length=50,null=True)
    articel_type = models.CharField(max_length=50,null=True)
    market_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    seller = models.ForeignKey(CompanyDetails, on_delete=models.SET_NULL,null=True)
    brand = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=200,null=True)
    size = models.CharField(max_length=5,default="S")
    material = models.CharField(max_length=200,null=True)
    completelook = models.TextField(null=True)
    
    def __str__(self):
        return self.title

class ProductImagesFiles(models.Model):
    product = models.ForeignKey(Product,on_delete=CASCADE)
    image_file = models.ImageField(upload_to="products",blank=True)

class ProductImagesURL(models.Model):
    product = models.ForeignKey(Product,on_delete=CASCADE)
    image_url = models.URLField(max_length=500,blank=True)
    

class Cart (models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "  CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Placed","Order Placed"),
    ("Order Processing","Order Processing"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),
    ("On the way","On the way")
)
    
class Sales(models.Model):
        company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        rate = models.PositiveIntegerField(default=0)
        quantity = models.PositiveIntegerField(default=0)
        subtotal = models.PositiveIntegerField(default=0)

        def __str__(self):
            return "Product: " + str(self.product) + " Sales: " + str(self.subtotal)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by =models.CharField(max_length=200)
    shipping_address =models.CharField(max_length=200)
    
    mob_no = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(blank=True)
    subtotal =models.PositiveIntegerField(null=True, blank=True)
    discount =models.PositiveIntegerField(null=True, blank=True)
    total =models.PositiveIntegerField(null=True, blank=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)
    
    