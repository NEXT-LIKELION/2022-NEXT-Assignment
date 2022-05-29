"""KUmap URL Configuration

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
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('first2/',views.first2, name='first3'),
    path('first3/',views.first3, name='first3'),
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3, name='test3'),
    path('entrance', views.entrance, name='entrance'),
    path('detail', views.detail, name='detail'),
    path('region', views.region, name='region'),

]
