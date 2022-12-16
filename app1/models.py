from django.db import models


class Card(models.Model):
    cname = models.CharField(max_length=100)
    cstock = models.IntegerField(default=1)
    cprice = models.IntegerField(default=1)
    cpicture = models.CharField(max_length=1000, default='default_picture')
