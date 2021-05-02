from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "apps.seller_accounts"
urlpatterns = [
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('signout/',views.signout, name="signout"),
    path('profile/',views.profile, name="profile"),
    path('company_info/',views.companyinfo, name="companyinfo"),
    path('company_sales/',views.companysales, name="companysales"),
    path('company_products/',views.companyproducts, name="companyproducts"),
    path('add_new_product/',views.addnewproduct, name="add_new_product"),
    path('company_details/',views.company_details, name="company_details"),
    path('addressinfo/',views.address_info, name="address_info")
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)