# -*- coding: utf-8 -*-
# @Time : 27/03/2021 10:15
# @Author : WANGKuo, XURui
# @File : views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from mysql.models import User
from mysql.models import Article
from mysql.models import Order
import hashlib

# Create your views here.
def login(request):
    """
    this is the login function.
    @param request: a new request to be executed.
    @return: a target page.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = hashlib.sha256(request.POST.get('pass').encode('utf-8')).hexdigest()
        res_user = User.objects.filter(user_name=username)
        if not res_user.exists():
            messages.success(request, "Username does not exist.")
            return render(request, 'login.html');
        if password == res_user[0].password:
            request.session['is_login'] = 'True'
            request.session['username'] = username
            return redirect('/index/')
    return render(request, 'login.html')

def logout(request):
    """
    the logout function
    @param request: a new request to be executed.
    @return:  return to the index page.
    """
    try:
        request.session.clear()
    except KeyError:
        pass
    return redirect('/index/')


def index(request):
    """
    Determine whether the user is logged in.
    @param request:
    @return: Return to different pages according to the user's different status.
    """
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
    """
    get an article according to the name.
    @param request:
    @param Name: article's name
    @return: an article object to the 'detail.html'.
    """
    print(Name)
    art = Article.objects.get(art_name=Name)
    return render(request, 'detail.html',{'article': art})


def rentals(request):
    """
    make an order.
    @param request:
    @return: return to the different page according to the user's state
    """
    is_login = request.session.get('is_login', False)
    if is_login:
        user_name = request.session.get('username')
        res_user = User.objects.get(user_name=user_name)
        orders = Order.objects.filter(id_user=res_user.id)
        return render(request, 'rentals.html',{'orders': orders})
    else:
        return render(request, 'rentals.html')


def register(request):
    """
    User registration interface
    @param request:
    @return: Register.html
    """
    return render(request, 'Register.html')


def addUser(request):
    """
    insert a user to the db
    @param request:
    @return: return to the login.html
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = hashlib.sha256(request.POST.get('pass').encode('utf-8')).hexdigest()
        email = request.POST.get('email')
        address = request.POST.get('address')
        user = User(user_name=username, mail=email, password=password,adress=address)
        user.save()
    return render(request, 'login.html')


def changePass(request):
    """
    change the password
    @param request:
    @return: login.html
    """
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            user = User.objects.get(user_name=str(username))
        except User.DoesNotExist:
            return render(request, 'ForgetPassword.html', {'messages': 0})

        newPassword = hashlib.sha256(request.POST.get('pass').encode('utf-8')).hexdigest()

        user.password = newPassword
        user.save()
    return render(request, 'login.html')

def switchFunction(request):
    """
    use different function according to the different url.
    @param request:
    @return: a html page.
    """
    if request.path == '/addUser/':
        return render(request, 'Register.html')
    if request.path == '/forgetPassword/':
        return render(request, 'ForgetPassword.html', {'messages': 1})
    return render(request, 'Register.html')


def rent(request, Name):
    """
    Rent a device (look up an object from the database)
    @param request:
    @param Name: the article's name
    @return: return to the rent.html with article
    """
    print(Name)
    art = Article.objects.get(art_name=Name)
    return render(request, 'rent.html', {'article': art})


def rent_art(request,Name):
    """
    Save order information
    @param request:
    @param Name: the articles'name
    @return: return to rent.html
    """
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

def show_profil(request, user_name):
    """
    show user's information
    @param request:
    @param user_name: username
    @return: profil.html
    """
    user = User.objects.get(user_name = user_name)
    orders = Order.objects.filter(id_user = user.pk)
    return render(request, 'profil.html', {'user': user, 'orders': orders, 'page': 0})

def changePage(request,user_name):
    """
    show the order's information
    @param request:
    @param user_name: username
    @return: profile.html with the informations
    """
    user = User.objects.get(user_name = user_name)
    orders = Order.objects.filter(id_user = user.pk)
    return render(request, 'profil.html', {'user': user, 'orders': orders, 'page': 1})