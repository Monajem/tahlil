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


def home_register(request):
    return render(request, 'main/home-register.html')

def user_home_rented(request):
    return render(request, 'main/user-home-rented.html')


def profile(request):
    return render(request, 'main/profile-base.html')

def user_home_renting(request):
    return render(request, 'main/user-home-renting.html')

def user_home_active(request):
    return render(request, 'main/user-home-active.html')

def about(request):
    return render(request, 'main/about.html')

def home_detail(request):
    return render(request, 'main/home-detail.html')

def staty(request):
    return render(request, 'main/staty.html')
