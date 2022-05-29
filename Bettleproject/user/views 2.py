from tkinter import E
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .riot_api import getSummonerInfo


DEVELOPMENTAPIKEY = "RGAPI-97f2ed81-4bee-4975-a55f-74510d188521"
# summonerName = "ㅂㄷㄱ"

# Create your views here.


def home(request, username):
    current_user = User.objects.get(username=username)
    context = {"current_user": current_user}
    return render(request, "home.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        summoner_name = request.POST["summoner_name"]
        summoner_data = getSummonerInfo(DEVELOPMENTAPIKEY, summoner_name)
        summoner_nick = summoner_data["name"]
        summoner_encypted_id = summoner_data["id"]
        summoner_puuid = summoner_data["puuid"]
        if "status" in summoner_data:
            context = {"summoner_error_msg": "유효하지 않는 소환사명입니다."}
            return render(request, "signup.html", context)
        found_user = User.objects.filter(username=username)
        if password != password2:
            password_error_msg = "두 비밀번호가 일치하지 않습니다."
            return render(
                request,
                "signup.html",
                {"password_error_msg": password_error_msg, "username": username},
            )
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "signup.html", {"error": error})
        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=summoner_nick,
            last_name=summoner_puuid,
        )
        auth.login(request, new_user)
        return redirect("home", username)
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        print("g")
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home", username)
        error = "아이디 또는 비밀번호가 틀립니다."
        context = {"error": error}
        return render(request, "login.html", context)
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")


# def validation(request):
#     matchs = getMatchsInfo(DEVELOPMENTAPIKEY, summoner_name)
