from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/<str:username>", views.home, name="home"),
]
