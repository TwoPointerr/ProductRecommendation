
from django.contrib import admin
from django.urls import path
from apps.main import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "apps.main"
urlpatterns = [
    path('',views.index, name="index"),
    path('category/',views.category, name="category"),
    
    path('allproducts', views.show_all_products, name="showallproducts"),
    path('filter-data/', views.filter_data, name="filter_data"),
    path('filter-auto/', views.filter_auto, name="filter_auto"),

    path("search_result/<str:keyword>", views.Search_Result,  name = "search_result"),
    path("search/", views.Search_Product,  name = "search_product"),
    path("single_product/<int:pid>/", views.Single_Product,  name = "single_product"),

    path("contact", views.Contact,  name = "contact"),
    path("reviews/<int:prodid>/", views.reviews, name="reviews")
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)