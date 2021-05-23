from django.db import models
from apps.accounts.models import *
from apps.cart.models import *
import datetime
from django.contrib.auth.models import User
# Create your models here.

class CustomerQueries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    phonenumber = models.CharField(max_length=10, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    rating = models.IntegerField(null=True)
    review = models.TextField()
    pros = models.TextField()
    cons = models.TextField()
    created_at = models.DateTimeField(auto_now = True, null=True)
