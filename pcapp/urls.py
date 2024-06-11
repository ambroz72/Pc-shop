from django.contrib import admin
from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path('',views.allproduct,name='allproduct'),
    path('<slug:c_slug>/',views.allproduct,name='product_by_category'),
    
]
