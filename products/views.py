from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    products = ["Ford", "Volvo", "BMW", "Toyota", "Mazda"]
    context = {
        'products': products
    }
    return render(request,'products/index.html', context)

def detail(request, id):
    context = {
        'id': id
    }
    return render(request,'products/detail.html', context)

def addShoppingCard(request, id):
    data = {
        'id': int(id)
    }
    return render(request,'products/addShoppingCard.html', data)
