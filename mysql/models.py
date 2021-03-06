# -*- coding: utf-8 -*-
# @Time : 27/03/2021 10:15
# @Author : WANGKuo, XURui
# @File : models.py
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=32)
    mail = models.EmailField()
    password = models.CharField(max_length=128)
    adress = models.TextField()
    class Meta:
        db_table = 'user'

class Article(models.Model):
    art_name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.CharField(max_length=256)
    stock = models.IntegerField()
    type = models.CharField(max_length=32)
    rate = models.IntegerField()
    class Meta:
        db_table = 'article'

class Order(models.Model):
    id_user = models.ForeignKey("User", on_delete=models.CASCADE)
    id_article = models.ForeignKey("Article", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'order'
