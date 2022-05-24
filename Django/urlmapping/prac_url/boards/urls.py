from django.urls import path
from boards import views

urlpatterns = [
    path('', views.boards),
    path('first/', views.boardfirst),
]