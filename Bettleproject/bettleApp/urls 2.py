from django.contrib import admin
from django.urls import path
from bettleApp import views

urlpatterns = [
    # path("login", views.login, name="login"),
   path("teamadd", views.teamadd, name="teamadd"),
   path("teamlist", views.teamlist, name="teamlist"),
   path("matchinfo/<int:team_pk>", views.matchinfo, name="matchinfo"),
   path("home/<str:username>", views.home, name="home"),
]
