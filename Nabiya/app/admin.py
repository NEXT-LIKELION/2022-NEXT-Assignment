from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Emotion, Tag, Pet, Diary, Post, Comment, Todo])

