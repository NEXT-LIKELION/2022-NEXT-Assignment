from django.shortcuts import render, redirect
from .models import School, Info, Lounge, Door
from django.core import serializers
import json
# Create your views here.

def index(request):
    schoolList = School.objects.all()
    schools = serializers.serialize('json', School.objects.all())
    # print(schools.replace('\r\n', ''))
    # print(type(schools))
    jsonObj = json.loads(schools)
    # print(jsonObj[0])
    # print(type(jsonObj[0]))
    schools = json.loads(schools)
    for i, v in enumerate(schools):
        # print(jsonObj[i]["fields"]["information"])
        if jsonObj[i]["fields"]["information"]:
            jsonObj[i]["fields"]["information"] = jsonObj[i]["fields"]["information"].replace('\r\n','\\n')
    
    # jsonObj[0]["fields"]["information"] = jsonObj[0]["fields"]["information"].replace('\r\n','\\r\n')
    # print('G')
    # print(schoolList)
    # print(schools)
    # print('a')
    jsonObj = json.dumps(jsonObj)
    # print(jsonObj)
    return render(request, 'index.html', {'schools': jsonObj, 'schoolList': schoolList})

def entrance(request, school_pk):
    doors = Door.objects.filter(building__pk=school_pk)
    infos = Info.objects.filter(school__pk=school_pk)
    school = School.objects.get(pk=school_pk)
    print(school)
    schoolj = serializers.serialize('json', [School.objects.filter(pk=school_pk)[0]])
    doorsj = serializers.serialize('json', Door.objects.filter(building__pk=school_pk))
    return render(request, 'entrance.html', {'school': school, 'schoolj': schoolj, 'doors': doors, 'infos': infos, 'doorsj': doorsj})

def first(request):
    return render(request, 'first.html')

def first2(request):
    return render(request, 'first2.html')

def first3(request):
    return render(request, 'first3.html')

def facility(request, school_pk):
    school = School.objects.get(pk=school_pk)
    lounges = school.lounge.all()
    print(lounges)

    return render(request, 'facility.html', {'school': school, 'lounges': lounges})

def route1(request):
    return render(request, '6.html')

def route2(request):
    return render(request, '2.html')

def route3(request):
    return render(request, '13.html')  