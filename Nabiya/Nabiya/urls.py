"""Nabiya URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.start, name='start'),
    path('home', views.home, name='home'), # 첫 달력화면
    path('add_pet', views.add_pet, name='add_pet'),


    path('new_diary/<str:date>', views.new_diary, name='new_diary'),
    path('list_diary', views.list_diary, name='list_diary'),

    path('register/login', views.login, name='login'), 
    path('register/signup', views.signup, name='signup'), # 로그인 화면에서 가입하기 버튼 클릭 시 연결
    path('register/logout', views.logout, name='logout'),

    
    path('list_tag', views.list_tag, name='list_tag'),
    path('delete_tag/<int:tag_pk>', views.delete_tag, name='delete_tag'),

    path('add_todo/<str:date>', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_pk>/<str:date>', views.delete_todo, name='delete_todo'),

    path('day_detail/<str:date>', views.day_detail, name='day_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
