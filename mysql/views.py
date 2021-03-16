from django.contrib import messages
from django.http import response
from django.shortcuts import render, redirect
from mysql.models import User
from mysql.models import Article
from mysql.models import Order
import hashlib

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
    data = [1, 2]
    is_login = request.session.get('is_login', False)
    print('is_login::::::')
    print(is_login)
    articles = Article.objects.all()
    if is_login:
        username = request.session['username']
        print('username::::::')
        print(username)
        return render(request, 'index.html',{'articles': articles})
    else:
        return render(request, 'index.html',{'articles': articles})


def article(request, Name):
    print(Name)
    art = Article.objects.get(art_name=Name)
    return render(request, 'detail.html',{'article': art})


def rentals(request):
    is_login = request.session.get('is_login', False)
    if is_login:
        user_name = request.session.get('username')
        res_user = User.objects.get(user_name=user_name)
        orders = Order.objects.filter(id_user=res_user.id)
        return render(request, 'rentals.html',{'orders': orders})
    else:
        return render(request, 'rentals.html')


def register(request):
    return render(request, 'Register.html')


def addUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = hashlib.sha256(request.POST.get('pass').encode('utf-8')).hexdigest()
        email = request.POST.get('email')
        address = request.POST.get('address')
        user = User(user_name=username, mail=email, password=password,adress=address)
        user.save()
    return render(request, 'login.html')


def changePass(request):
    if request.method == "POST":
        username = request.POST.get('username')
        newPassword = request.POST.get('pass')
        user = User.objects.get(user_name = username)
        user.password = newPassword
        user.save()
    return render(request, 'login.html')


def switchFunction(request):
    if request.path == '/addUser/':
        return render(request, 'Register.html')
    if request.path == '/forgetPassword/':
        return render(request, 'ForgetPassword.html')
    return render(request, 'Register.html')


def rent(request, Name):
    print(Name)
    art = Article.objects.get(art_name=Name)
    return render(request, 'rent.html', {'article': art})


def rent_art(request,Name):
    print(Name)
    art = Article.objects.get(art_name=Name)
    nb_week = request.POST.get('nb')
    user_name = request.session.get('username')
    res_user = User.objects.get(user_name=user_name)
    order = Order(id_user=res_user,id_article=art)
    order.save()
    art.stock = art.stock - 1
    art.save()
    messages.success(request, "Rent success!")
    return render(request, 'rent.html', {'article': art})