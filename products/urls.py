from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^detail/(?P<id>[0-9]+)/add-shopping-card/$', views.addShoppingCard, name='detail')
]