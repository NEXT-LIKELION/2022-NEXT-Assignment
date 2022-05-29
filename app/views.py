from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Participation, Pig, Schedule
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required(login_url='/registration/login')
def home(request):
    now = datetime.datetime.now()
    pigs = Pig.objects.all()
    pigList = [];
    schedules = Schedule.objects.all().order_by('-when_to_meet')
    #schedules = Schedule.objects.all().order_by('-when_to_meet')

    for pig in pigs:
      if request.user.profile.pk == pig.host.pk:
        pigList.append(pig)  
      for participant in pig.participants.all():
        if request.user.profile.pk == participant.profile.pk:
          pigList.append(pig)

    impending_schedule = None
    for schedule in schedules:
      participants = [] 
      for i in schedule.pig_info.participants.all():
        participants.append(i.profile)
      if not request.user.profile in schedule.arrived.all() and request.user.profile in participants:
        impending_schedule = schedule

    pigList = set(pigList)
    if impending_schedule:
      if (impending_schedule.when_to_meet - datetime.datetime.now()).total_seconds()/60 > 30:
        impending_schedule = None
    
    total_late = 0
    for participation in request.user.profile.participation_set.all():
      total_late += participation.time_late

    return render(request, "home.html",{'pigs': pigList, 'impending_schedule': impending_schedule, 'total_late': total_late})


def signup(request):
    if request.method == "POST":
        profile = Profile()
        username = request.POST["username"]
        password = request.POST["password"]
        profile.nickname = request.POST["nickname"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 존재하는 아이디입니다."
            return render(request, "registration/signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        profile.user = new_user        

        profile.save()

        auth.login(request, new_user)

        return redirect("home")
    return render(request, "registration/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user)
            return redirect("home")
            
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "registration/login.html", {"error":error})
    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)

    return redirect("home")


@login_required(login_url="/registration/login")
def pig_new(request):
    if request.method == "POST":
        new_Pig = Pig.objects.create(
            pig_name = request.POST["pig_name"],
            host = request.user.profile,
            pig_description = request.POST["pig_description"],
            exchange_rate = request.POST["exchange_rate"],
        )
        participants_pk = request.POST.getlist('user_list');
        for i in participants_pk:
          print(i)
          new_participation = Participation()
          new_participation.profile = Profile.objects.get(pk=int(i)-1)
          new_participation.time_late = 0
          new_participation.save()
          new_Pig.participants.add(new_participation)
        return redirect('home')
    profiles = Profile.objects.all()
    return render(request, 'pig_new.html', {'profiles' : profiles})


# @login_required(login_url="/registration/login")
# def pig_new(request):
#     if request.method == "POST":
#         new_Pig = Pig.objects.create(
#             pig_name = request.POST["pig_name"],
#             host = request.user.profile,
#             pig_description = request.POST["pig_description"],
#             exchange_rate = request.POST["exchange_rate"],
#         )
#         participants_pk = request.POST.getlist('user_list');
#         for i in participants_pk:
#           new_participation = Participation()
#           new_participation.profile = Profile.objects.filter(pk=i)[0]
#           new_participation.time_late = 0
#           new_participation.save()
#           new_Pig.participants.add(new_participation)
#         return redirect('home')
#     profiles = Profile.objects.all()
#     return render(request, 'pig_new.html', {'profiles' : profiles})

@login_required(login_url="/registration/login")
def pig_detail(request, pig_pk):
    pig = Pig.objects.get(pk=pig_pk)
    schedules = Schedule.objects.filter(pig_info = pig_pk)
    participations = pig.participants.order_by('-time_late')
    total_late = 0
    time_late = 0
    for participation in participations:
      if participation.profile == request.user.profile:
        time_late = participation.time_late
      total_late += participation.time_late
    return render(request, 'pig_detail.html', {'profile': pig.host, 'pig': pig, 'schedules': schedules, 'time_late': time_late, 'participations': participations, 'total_late': total_late})


@login_required(login_url="/registration/login")
def schedule_new(request, pig_pk):
    if request.method =='POST':
      pig = Pig.objects.get(pk=pig_pk)
      new_schedule = Schedule.objects.create(
        pig_info = pig,
        schedule_name = request.POST['schedule_name'],
        schedule_description = request.POST['schedule_description'],
        where_to_meet = request.POST['where_to_meet'],
        when_to_meet =request.POST['when_to_meet'],
      )

      return redirect('addevent_complete') 
    return render(request, 'schedule_new.html', {"pig_pk": pig_pk})



@login_required(login_url="/registration/login")
def pig_bye(request, pig_pk):
    pig = Pig.objects.get(pk=pig_pk)
    total_late = 0
    for i in pig.participants.all():
      total_late += i.time_late
    return render(request, 'pig_bye.html', {'total_late': total_late})

# /**********************************************************/

@login_required(login_url="/registration/login")
def bye_donate(request):
    return render(request, 'bye_donate.html')


@login_required(login_url="/registration/login")
def bye_winner(request):
    
    return render(request, 'bye_winner.html')

# /**********************************************************/

@login_required(login_url="/registration/login")
def bye_winner_complete(request):
    return render(request, 'bye_winner_complete.html')


@login_required(login_url="/registration/login")
def bye_donate_complete(request):
    return render(request, 'bye_donate_complete.html')

@login_required(login_url="/registration/login")
def landing(request):
    return render(request, 'landing.html')

@login_required(login_url="/registration/login")
def arrive(request, schedule_pk):
  schedule = Schedule.objects.get(pk=schedule_pk)
  participations = Participation.objects.filter(profile = request.user.profile)
  participation = None
  for pa in participations:
    if pa.pig.all():
      if pa.pig.all()[0].pk == schedule.pig_info.pk:
        participation = pa

  schedule.arrived.add(request.user.profile)
  if schedule.when_to_meet < datetime.datetime.now():
    participation.time_late += int((datetime.datetime.now() - schedule.when_to_meet).total_seconds()/60)
    participation.save()
    

  return redirect('home')
def addevent_complete(request):
    return render(request,'addevent_complete.html')

def addpig_complete(request):
    return render(request,'addpig_complete.html')

