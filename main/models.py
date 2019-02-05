from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class House(models.Model):
    CITIES = (
        ('تهران', 'تهران'),
    )
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITIES, blank=True)
    address = models.TextField()
    room = models.IntegerField()
    price = models.IntegerField()
    space = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})