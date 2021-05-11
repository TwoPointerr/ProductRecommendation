from django.contrib import admin
from .models import CompanyAddress, CompanyDetails


admin.site.register([ CompanyAddress, CompanyDetails])
# Register your models here.
