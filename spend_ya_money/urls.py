from django.conf.urls import url

from spend_ya_money import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^callback/', views.callback, name='callback'),
]
