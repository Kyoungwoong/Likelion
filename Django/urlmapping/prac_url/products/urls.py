from django.urls import path
from products import views

urlpatterns = [
    path('', views.productlist),
    path('first/', views.productfirst),
    
]