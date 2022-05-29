from tkinter import E
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .riot_api import getSummonerInfo, getMatchsInfo, getOneMatchInfo
from .models import Bullet
from django.contrib.auth.decorators import login_required


DEVELOPMENTAPIKEY = "RGAPI-97f2ed81-4bee-4975-a55f-74510d188521"
# summonerName = "ㅂㄷㄱ"

# Create your views here.


def home(request, username):
    current_user = User.objects.get(username=username)
    bullet_num = Bullet.objects.get(owner__username=username)
    context = {"current_user": current_user, 'bullet_num':bullet_num.num}
    return render(request, "home.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        summoner_name = request.POST["summoner_name"]
        print(1)
        summoner_data = getSummonerInfo(DEVELOPMENTAPIKEY, summoner_name)
        print(2)
        summoner_nick = summoner_data["name"]
        summoner_encypted_id = summoner_data["id"]
        summoner_puuid = summoner_data["puuid"]
        if "status" in summoner_data:
            print(3)
            context = {"summoner_error_msg": "유효하지 않는 소환사명입니다."}
            return render(request, "signup.html", context)
        found_user = User.objects.filter(username=username)
        if password != password2:
            print(4)
            password_error_msg = "두 비밀번호가 일치하지 않습니다."
            return render(
                request,
                "signup.html",
                {"password_error_msg": password_error_msg, "username": username},
            )
        if len(found_user):
            print(5)
            error = "이미 아이디가 존재합니다"
            return render(request, "signup.html", {"error": error})
        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=summoner_nick,
            last_name=summoner_puuid,
        )
        print(6)
        new_bullet = Bullet.objects.create(num=30, owner=new_user)
        auth.login(request, new_user)
        return redirect("user:home", username)
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        print("g")
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("user:home", username)
        error = "아이디 또는 비밀번호가 틀립니다."
        context = {"error": error}
        return render(request, "login.html", context)
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")


# def validation(request):
#     matchs = getMatchsInfo(DEVELOPMENTAPIKEY, summoner_name)


@login_required(login_url="user/login/")
def reload_bullet(request):
    username = request.user.username
    bullet_now = Bullet.objects.get(owner__username=username)
    if request.method == "POST":
        bullet_reloaded = request.POST["bullet_reloaded"]
        num_reloaded = bullet_now.num + int(bullet_reloaded)
        Bullet.objects.update(num=num_reloaded)
        return redirect("user:home", username)
    context = {"username": username, "bullet_now": bullet_now}
    return render(request, "reload.html", context)