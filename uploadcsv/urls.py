from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postcsv/$', views.postcsv, name='postcsv'),
]
