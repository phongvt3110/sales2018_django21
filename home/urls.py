from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/news/', views.news, name='news'),
    path('home/contacts/', views.contacts, name='contacts'),
]
