from django.shortcuts import render
from products.models import Products

# Create your views here.
from django.http import HttpResponse

def index(request):
    data = {
        'body': 'layouts/sites/body.html',
        'advertisement': 'layouts/sites/advertisement.html'
    }
    return render(request,'home/index.html',data)
def news(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is News page")
    Products.objects.create(name="Iphone7",price=20000000)
    return response

def contacts(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is Contacts page")
    return response