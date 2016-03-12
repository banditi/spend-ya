from django.conf.urls import url

import views
from spend_ya_telegram.spend_ya_bot import start_bot

urlpatterns = [
    url(r'^(?P<telegram_token>[\w\W]+)', views.telehook, name='hook')
]

start_bot()
