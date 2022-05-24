"""prac_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second/', views.second),
    path('products/', include('products.urls')), # products로 시작하는 주소는 모두 products.urls에서 관리하겠다.
    path('boards/', include('boards.urls')),
]

# 상품관련 URL
    # http://127.0.0.1:8000/products/1
    # http://127.0.0.1:8000/products/2
    # http://127.0.0.1:8000/products/3

# 게시판 URL
    # http://127.0.0.1:8000/boards/1
    # http://127.0.0.1:8000/boards/2
    # http://127.0.0.1:8000/boards/3    
