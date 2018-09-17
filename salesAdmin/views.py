from django.shortcuts import render

def index(request):
    return render(request, 'salesAdmin/index.html')

def demo(request):
    return render(request, 'salesAdmin/demo.html')
