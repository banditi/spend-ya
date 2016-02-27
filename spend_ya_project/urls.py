from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import spend_ya_telegram.views
import views

# Examples:
# url(r'^$', 'spend_ya_telegram.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^db', spend_ya_telegram.views.db, name='db'),
    # url(r'^admin/', include(admin.site.urls)),
]
