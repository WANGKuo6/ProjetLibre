from django.http import HttpResponse

from mysql.models import *
def insertUser(request):
    user = User(user_name='smith', mail='smith@gmail.com', password='123',adress='grandmont batiment G, 37000 tours')
    User1 = User(user_name='trump', mail='trump@gmail.com', password='456',adress='white house')
    User2 = User(user_name='putin', mail='putin@gmail.com', password='137', adress='Kremlin and Red Square')
    User3 = User(user_name='macron', mail='macron@gmail.com', password='139', adress='Elysee Palace')
    user.save()
    User1.save()
    User2.save()
    User3.save()

    article = Article(art_name='iphone12', description='the latest version of iphone', image='')
    return HttpResponse("<p>add success！</p>")

