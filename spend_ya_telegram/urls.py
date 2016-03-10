from django.conf.urls import url

import views


urlpatterns = [
    url(r'^(?P<telegram_token>[\w\W]+)', views.telehook, name='hook')
]
