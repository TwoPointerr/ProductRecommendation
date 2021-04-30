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
    path('address/',views.address, name="address")
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)