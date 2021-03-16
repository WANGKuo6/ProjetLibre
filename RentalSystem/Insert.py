from datetime import timezone

from django.http import HttpResponse
import hashlib

from mysql.models import *
def insertUser(request):
    user = User(user_name='smith', mail='smith@gmail.com', password=hashlib.sha256('123'.encode('utf-8')).hexdigest(), adress = 'grandmont batiment G, 37000 tours')
    user1 = User(user_name='trump', mail='trump@gmail.com', password=hashlib.sha256('456'.encode('utf-8')).hexdigest(),adress='white house')
    user2 = User(user_name='putin', mail='putin@gmail.com', password=hashlib.sha256('137'.encode('utf-8')).hexdigest(), adress='Kremlin and Red Square')
    user3 = User(user_name='macron', mail='macron@gmail.com', password=hashlib.sha256('139'.encode('utf-8')).hexdigest(), adress='Elysee Palace')
    user.save()
    user1.save()
    user2.save()
    user3.save()

    return HttpResponse("<p>add success！</p>")

