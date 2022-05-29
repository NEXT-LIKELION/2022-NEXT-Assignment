from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .models import Team
# Create your views here.

@login_required(login_url="/user/login")
def teamadd(request): 
    if request.method == "POST":
        team = Team.objects.create(
            hostUser = request.user,
            firstMember = request.POST["firstMember"],
            secondMember = request.POST["secondMember"],
            thirdMember = request.POST["thirdMember"],
            fourthMember = request.POST["fourthMember"],
            Tier = request.POST["Tier"],
            bulletBet = request.POST["bulletBet"],
        )
        match_dates = request.POST.getlist('match_dates[]')
        team.set_matchDates(match_dates)
        print('날짜정보', team.get_matchDates())
        return redirect('teamlist')
    return render(request, 'teamadd.html')

def teamlist(request):
    teams = Team.objects.all()
    return render(request, 'teamlist.html', {'teams' : teams})

def matchinfo(request,team_pk):
    info_team = Team.objects.get(pk=team_pk)
    return render(request, 'matchinfo', {'info_team' : info_team})

# def waiting(request):
#     return render(request, 'waiting.html')
    
    
def home(request, username):
    current_user = User.objects.get(username=username)
    context = {"current_user": current_user}
    return render(request, "home.html", context)
