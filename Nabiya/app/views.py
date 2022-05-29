from asyncore import write
from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core import serializers
from django.utils.dateparse import parse_date
from datetime import date

from django.contrib.auth.decorators import login_required
from .models import *
import json
# Create your views here.

def start(request):
    return render(request, 'start.html')

@login_required(login_url='register/login')
def home(request):
    diarys = serializers.serialize("json", Diary.objects.all())
    return render(request, 'home.html', {'diarys':diarys})

def add_pet(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        new_pet = Pet.objects.create(
            owner = user,
            profile_img = request.FILES["profile_img"],
            name = request.POST["name"],
            birth = request.POST["birth"],
            introduction = request.POST.get("introduction"),
        )

        if new_pet.species == 'C':
            after_birth = date.today() - date(new_pet.birth)

        return redirect("home")
    return render(request, "add_pet.html")


def new_diary(request, date):
    if request.method == "POST" :
        user = User.objects.get(username=request.user)
        emotion = Emotion.objects.get(status=request.POST['emotion'])
        new_post = Diary.objects.create(
            writer = user,
            emotion = emotion,
            content = request.POST["content"],
            photo = request.FILES.get('photo'),
            uploaded = date
        )
        return redirect("day_detail", date)
    return render(request, "new_post.html")


def list_diary(request):
    diarys = Diary.objects.all()
    datas = []
    for diary in diarys:
        datas.append([diary, diary.writer.pets.all().first()])
    return render(request, 'list_diary.html', {'datas':datas})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            # return redirect(request.GET.get("next","/"))
            return redirect("home")
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})

    return render(request, "registration/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 존재하는 아이디입니다"
            return render(request,"registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect('add_pet')
    return render(request, "registration/signup.html")

def logout(request):
    auth.logout(request)

    return redirect("start")

@login_required(login_url='register/login')
def add_tag(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        new_tag = Tag.objects.create(
            name=request.POST['name'],
            color=request.POST['color'],
            writer=user
        )
        return redirect('list_tag')
    return render(request, 'add_tag.html')

def list_tag(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        new_tag = Tag.objects.create(
            name=request.POST['name'],
            writer=user
        )
        return redirect('list_tag')
    return render(request, 'list_tag.html')


def delete_tag(request, tag_pk):
    tag = Tag.objects.get(pk=tag_pk)
    tag.delete()
    return redirect('list_tag')

def day_detail(request, date):
    diary_query = Diary.objects.filter(uploaded=parse_date(date))
    todos = Todo.objects.filter(date=parse_date(date))
    diary = diary_query[0] if diary_query.count() > 0 else diary_query
    return render(request, 'day_detail.html', {'diary':diary, 'date':date, 'todos':todos})


@login_required(login_url='register/login')
def add_todo(request, date):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        tag_pks = request.POST.getlist('tag')

        for tag_pk in tag_pks:
            tag = Tag.objects.get(pk=tag_pk)
            found_todo = Todo.objects.filter(date=parse_date(date), tag=tag)
            if found_todo.count() > 0:
                continue
            
            new_todo = Todo.objects.create(
                writer=user,
                date=parse_date(date),
                tag=tag
            )

        return redirect('day_detail', date)
    return render(request, 'add_todo.html')

@login_required(login_url='register/login')
def delete_todo(request, todo_pk, date):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('day_detail', date)