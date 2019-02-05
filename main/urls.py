from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.login, name="login"),
    # path('register', views.register, name="register"),
    path('result', views.result, name="result"),
    path('home-register', views.home_register, name="home-register"),
    path('user-home-rented', views.user_home_rented, name="user-home-rented"),
    path('profile', views.profile, name='profile'),
    path('user-home-renting', views.user_home_rented, name="user-home-renting"),
    path('user-home-active', views.user_home_active, name="user-home-active"),
    path('about', views.about, name="about"),
    path('home-detail', views.home_detail, name="home-detail"),
    path('staty', views.staty, name="staty"),


]