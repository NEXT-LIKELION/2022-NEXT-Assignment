from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("profileEdit/", views.profileEdit, name="profileEdit"),
    path("notice/", views.notice, name="notice"),
    path("noticeDetail/", views.noticeDetail, name="noticeDetail"),
    path("sendMail/", views.sendMail, name="sendMail"),
    path("sendCategoryMail/", views.sendCategoryMail, name="sendCategoryMail"),
]