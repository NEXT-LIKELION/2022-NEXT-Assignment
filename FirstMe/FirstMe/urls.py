"""FirstMe URL Configuration

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
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 홈페이지
    path('', views.home, name="home"),
    # #로그인 페이지
    path('registration/login/', views.login, name="login"),
    # 회원가입 페이지
    path('registration/signup/', views.signup, name="signup"),
    # 로그아웃
    path('registration/logout/', views.logout, name="logout"),
    # 내 명함 만들기 페이지 (1, 2로 나뉘어서 필수와 선택 보이게 할 것)
    path('make/', views.make, name="make"),
    # 내 명함 디테일 페이지
    path('mycard/<slug:card_link>/', views.detail, name="detail"),
    # 내 명함 수정 페이지
    path('mycard/<slug:card_link>/edit', views.edit, name="edit"),
    # 그룹 디테일
    path('group/<int:group_pk>/', views.group_detail, name="group_detail"),
    # 내 명함 1대1 초대 페이지
    path('<slug:card_link>/<int:access_code>/', views.personal_invitation, name="personal_invitation"),
    # 그룹 만들기 페이지(그룹 이름 입력하는 칸)
    path('make_group/', views.make_group, name="make_group"),
    # 그룹 초대 페이지
    path('group/<int:group_pk>/<int:access_code>/', views.group_invitation, name="group_invitation"),
   
    # 그룹 목록
    path('<slug:card_link>/group_list/', views.group_list, name="group_list"),
    # 친구 목록
    path('<slug:card_link>/friend_list/', views.friend_list, name="friend_list"),

]