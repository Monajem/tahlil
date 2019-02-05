from django.urls import path
from . import views
from .views import HouseListView, HouseCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('result', HouseListView.as_view() , name="house-list"),
    path('home-register', HouseCreateView.as_view(), name="home-register"),
    path('about', views.about, name="about"),
    path('home-detail', views.home_detail, name="home-detail"),
]