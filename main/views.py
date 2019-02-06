from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import House, Rent
from .forms import RentForm, SearchForm
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
    fields = ['title', 'city', 'address', 'space', 'room', 'price', 'comment']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class HouseDetailView(DetailView):
    model = House
    context_object_name = 'house'


def about(request):
    return render(request, 'main/about.html')


def staty(request):
    return render(request, 'main/staty.html')


def rent(request, pk):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            new_tx = Rent.objects.create(
                user = request.user,
                house = House.objects.get(pk=pk),
                begin_date = form.cleaned_data['begin_date'],
                end_date = form.cleaned_data['end_date'],
            )
            tx_id = new_tx.id
            house = House.objects.get(pk=pk)
            house.reserved +=1
            house.save()
            return render(request, 'main/pay.html', {'tx_id': tx_id})
    else:
        form = RentForm()
    return render(request, 'main/rent_home.html', context={'form': form})


def pay(request, pk):
    tx = Rent.objects.get(pk=pk)
    tx.paid = True
    tx.save()
    return redirect('rent-success')


def rent_success(request):
    return render(request, "main/rent-success.html")


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            houses = House.objects.filter(city=city).order_by('-reserved')
            return render(request, "main/house_list.html", {'houses': houses})

    form = SearchForm()
    return render(request, "main/search.html", {'form' : form})