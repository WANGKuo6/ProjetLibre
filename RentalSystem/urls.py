"""RentalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysql import views
from . import Insert
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', Insert.insertUser),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('detail/<Name>/', views.article, name='urlName'),
    path('rentals', views.rentals),
    path('register/', views.switchFunction),
    path('addUser/', views.addUser),
    path('changePass/', views.changePass),
    path('forgetPassword/', views.switchFunction),
    path('rent/<Name>/', views.rent, name='Name'),
    path('rent_art/<Name>/', views.rent_art, name='art'),
    path('profil/<user_name>',views.show_profil, name='user_name'),
    path('change/<user_name>', views.changePage, name='user_name'),
    path('', views.index)
]

