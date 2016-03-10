from __future__ import unicode_literals
from django.apps import AppConfig
from spend_ya_bot import start_bot


class SpendYaTelegramConfig(AppConfig):
    name = 'spend_ya_telegram'

    def ready(self):
        start_bot()
