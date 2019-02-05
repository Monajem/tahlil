from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import House
# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def result(request):
    return render(request, 'main/house_list.html')


class HouseListView(ListView):
    model = House
    context_object_name = 'houses'


class HouseCreateView(CreateView):
    model = House
    fields = ['title', 'city', 'address', 'room', 'price', 'comment']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'main/about.html')


def home_detail(request):
    return render(request, 'main/home-detail.html')

