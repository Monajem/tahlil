from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')


def result(request) :
    return render(request, 'main/result.html')
