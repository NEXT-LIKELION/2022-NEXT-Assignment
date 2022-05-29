from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test2(request):
    return render(request, 'index2.html')

def test1(request):
    return render(request, 'index.html')

def test3(request):
    return render(request, 'index3.html')

def first(request):
    return render(request, 'first.html')

def first2(request):
    return render(request, 'first2.html')

def first3(request):
    return render(request, 'first3.html')

def entrance(request):
    return render(request, 'entrance.html')

def detail(request):
    return render(request, 'detail.html')

def region(request):
    return render(request, 'region.html')