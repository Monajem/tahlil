from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class House(models.Model):
    CITIES = (
        ('تهران', 'تهران'),
        ( 'اراک', 'اراک'),
        ('سنندج', 'سنندج'),
        ('یاسوج', 'یاسوج'),
        ('بوشهر', 'بوشهر'),
        ('جم', 'جم'),
        ('اصفهان', 'اصفهان'),
        ('تبریز', 'تبریز'),
        ('قزوین', 'قزوین'),
        ('مشهد', 'مشهد'),
        ('سازی','سازی'),
        ('بیرجند', 'بیرجند'),
        ('زاهدان', 'زاهدان'),
        ('کرمان', 'کرمان'),
        ('زابل', 'زابل'),
        ('اهواز', 'اهواز'),
        ('آبادان', 'آبادان'),
        ('قم', 'قم'),
        ('کرمانشاه', 'کرمانشاه'),
        ('ایلام', 'ایلام'),
        ('ساوه', 'ساوه'),
        ('قائن', 'قائن'),
        ('قوچان', 'قوچان'),
        ('یزد', 'یزد'),
        ('شیراز', 'شیراز'),
        ('رشت', 'رشت'),
        ('شهرکرد', 'شهرکرد'),
        ('طبس', 'طبس'),
        ('نیشابور', 'نیشابور'),
        ('ری', 'ری'),
        ('کرج', 'کرج'),
        ('سمنان', 'سمنان'),
        ('شاهرود', 'شاهرود'),
        ('سبزوار', 'سبزوار'),
    )
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITIES, blank=True)
    address = models.TextField()
    room = models.IntegerField()
    price = models.IntegerField()
    space = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    reserved = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})


class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField()
    paid = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'house', 'begin_date', 'end_date'))