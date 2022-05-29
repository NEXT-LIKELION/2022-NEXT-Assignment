from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from bettleApp.models import Team

# Create your views here.
from .riot_api2 import getOneMatchInfo

DEVELOPMENTAPIKEY = "RGAPI-97f2ed81-4bee-4975-a55f-74510d188521"

def gaming(request):
    return render(request, "gaming.html")

def game_result(request):
    username = request.user
    print(username)
    current_user = User.objects.get(username=username)
    print(current_user.last_name)
    summonerName = current_user.first_name
    summonerPuuid = current_user.last_name
    last_match_info = getOneMatchInfo(DEVELOPMENTAPIKEY, summonerName, 0)
    participants = last_match_info["metadata"]["participants"]
    if participants.index(summonerPuuid) < 5:
        team_index = 0
    else:
        team_index = 1
    game_result = last_match_info["info"]["teams"][team_index]["win"]
    print(game_result)
    context = {"game_result": game_result, "username": username}
    return render(request, "test.html", context)