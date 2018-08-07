from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is Product list page")
    return response

def detail(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is Product detail page")
    return response