from django.contrib import admin
from django.urls import path
from resultApp import views

app_name = "resultApp"

urlpatterns = [
    path("gaming", views.gaming, name="gaming"),
    path("test", views.game_result, name="test")
]