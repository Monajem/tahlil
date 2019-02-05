from django.db import models
from django.contrib.auth.models import User


class House(models.Model):
    CITIES = (
        ('تهران', 'تهران'),
    )
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITIES, blank=True)
    address = models.TextField()
    room = models.IntegerField()
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
