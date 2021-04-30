from django.db import models
from apps.accounts.models import *
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    market_price =models.PositiveIntegerField()
    selling_price =models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count =models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Cart (models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
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
        return "Cart: " + str(Cart.id) + " CartProduct: " + str(self.id)

ORDER_STATUS = (
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("Order Completed","Order Completed"),
    ("Order Canceled","Order Canceled"),
    ("On the way","On the way")
)
class Order(models.Model):
    Cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by =models.CharField(max_length=200)
    shipping_address =models.CharField(max_length=200)
    mobile =models.CharField(max_length=10)
    subtotal =models.PositiveIntegerField()
    discount =models.PositiveIntegerField()
    total =models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)
    
    
    
    