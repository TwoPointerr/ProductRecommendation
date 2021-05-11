from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CompanyDetails(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_email = models.EmailField()
    company_desc = models.TextField()
    company_number = models.CharField(max_length=12,null=True, blank=True)
    def __str__(self):
        return f'{self.user.username} {self.company_name}'


class CompanyAddress(models.Model):
    company = models.OneToOneField(CompanyDetails, on_delete=models.CASCADE)
    addline = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField()
    def __str__(self):
        return self.city + " - " + self.pincode


