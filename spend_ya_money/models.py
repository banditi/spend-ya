from __future__ import unicode_literals

from django.db import models
from spend_ya_telegram.models import User


class Wallet(models.Model):
    account = models.TextField(blank=False, unique=True)
    access_token = models.TextField(blank=False)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)
    user = models.ForeignKey(User)
    card_id = models.CharField(blank=True, max_length=20)
