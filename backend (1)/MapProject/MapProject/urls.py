"""MapProject URL Configuration

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
from MapApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('first2/', views.first2, name='first2'),
    path('first3/', views.first3, name='first3'),
    path('index/', views.index, name='index'),
    path('entrance/<int:school_pk>', views.entrance, name="entrance"),
    path('facility/<int:school_pk>', views.facility, name="facility"),
    path('index/6/', views.route1, name='6'),
    path('index/2/', views.route2, name='2'),
    path('index/13/', views.route3, name='13'),
]