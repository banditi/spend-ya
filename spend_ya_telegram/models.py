from __future__ import unicode_literals

from django.db import models

from spend_ya_money.models import YaMoney


class Expenditure(models.Model):
    amount = models


class User(models.Model):
    uid = models.IntegerField(blank=False, unique=True)
    username = models.TextField(blank=False)
    wallet = models.ManyToManyField(YaMoney)
    expenditure = models.ManyToManyField(Expenditure)
