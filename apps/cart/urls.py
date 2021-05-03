
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "apps.cart"
urlpatterns = [
    
    path('addtocart-<int:pid>/',views.addtocart, name="addtocart"),
    path('my-cart/',views.mycart, name="mycart"),
    path("managecart/<int:cpid>/", views.managecart, name="managecart"),
    path("emptycart/", views.emptycart, name="emptycart"),
    path("checkoutdetails/", views.checkoutdetails, name="checkoutdetails")

]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)