from django.shortcuts import render
from products.models import Products

def index(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request,'products/index.html', context)

def detail(request, id):
    product = Products.objects.get(pk=id)
    context = {
        'product': product
    }
    return render(request,'products/detail.html', context)

def addShoppingCard(request, id):
    data = {
        'id': int(id)
    }
    return render(request,'products/addShoppingCard.html', data)
