from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is Home page")
    return response

def news(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is News page")
    return response

def contacts(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is Contacts page")
    return response