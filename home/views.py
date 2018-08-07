from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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