from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    uid = models.IntegerField(blank=False, unique=True)
    username = models.TextField(blank=False)
    password = models.CharField(blank=True, max_length=30)
