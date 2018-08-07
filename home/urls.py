# code style version Django 1.11

# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url('', views.index, name='index'),
# ]

# code style from Django 2.0 version

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/news/', views.news, name='news'),
    path('home/contacts/', views.contacts, name='contacts'),
]
