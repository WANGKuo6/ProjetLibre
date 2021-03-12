from django.http import response
from django.shortcuts import render, redirect
from mysql.models import *


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        res_user = User.objects.get(user_name=username)
        if password == res_user.password:
            request.session['is_login'] = 'True'
            request.session['username'] = username
            return redirect('/index/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    try:
        request.session.clear()
    except KeyError:
        pass
    return redirect('/index/')


def index(request):
    print('666')
    is_login = request.session.get('is_login', False)
    print('is_login::::::')
    print(is_login)
    if is_login:
        username = request.session['username']
        print('username::::::')
        print(username)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

