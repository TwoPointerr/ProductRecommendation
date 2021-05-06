from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "apps.accounts"
urlpatterns = [
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('signout/',views.signout, name="signout"),
    path('profileset/',views.profileset, name="profileset"),
    path('profile/',views.acprofile, name="profile"),
    path('shippingset/',views.shippingset, name="shippinginfo"),
    path('address/',views.address, name="address"),
    path('manageadd/<int:addid>/',views.manageadd, name="manageadd"),
    path('orders/',views.orders, name="orders"),
    path('order-<int:orderid>/',views.orderdetail, name="orderdetail")
    
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)