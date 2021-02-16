from django.shortcuts import render, redirect
from mysql.models import *

# Create your views here.
def login(request):
    print("123")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        res_user = User.objects.get(user_name=username)
        if password == res_user.password:
            print("456")
            return redirect('/index/')
    return render(request, 'login.html')

def index(request):
    return render(request, 'Login.html')

def Accueil(request):
    return render(request, 'index.html')