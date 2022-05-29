"""YouAndI URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    # path('usersignup', views.user_create, name='usersignup'),
    path('userlogin', views.user_create, name='userlogin'),
    
    path('testcreate/<int:user_pk>', views.test_create, name='testcreate'),
    path('testcheck/<int:test_pk>', views.test_checksend, name='testcheck'),
    
    path('lobby/<int:test_pk>', views.lobby, name = 'lobby'),

    path('guestlogin/<int:test_pk>', views.guest_create, name='guestlogin'),
    path('dotest/<int:test_pk>/<int:guest_pk>', views.test_load, name='dotest'),
    # path('result/<int:test_pk>/<int:gtest_pk>', views.test_result, name='result'),
    path('result/<int:test_pk>/<int:guest_pk>', views.test_result, name='result'),
    path('final/<int:number>', views.test_final, name='final')


    
]
