from django.contrib import admin
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("login", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("home/<str:username>", views.home, name="home"),
    path("logout", views.logout, name="logout"),
    path("reload/", views.reload_bullet, name="reload")
]