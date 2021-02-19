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
            #rep.set_cookie("user",username)
            context = {
                'user_login': username,
            }
            rep = render(request,'index.html',context)
            return rep
    return render(request, 'login.html')


def logout(request):
    context = {
    }
    return render(request, 'index.html',context)


def index(request):
    return render(request, 'index.html')


def Accueil(request):
    return render(request, 'index.html')