from django.shortcuts import render

def index(request):
    user = {
        'name': "Phongvt",
        'phone': "0983397580"
    }
    data = {
        'user': user,
        'role': "admin-role"
    }
    return render(request, 'backend/index.html', data)