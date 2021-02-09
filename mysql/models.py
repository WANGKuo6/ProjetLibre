from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=32)
    mail = models.EmailField()
    password = models.CharField(max_length = 32)
    adress = models.TextField()
    class Meta:
        db_table = 'user'

class Article(models.Model):
    art_name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.CharField(max_length=32)
    stock = models.IntegerField()
    type = models.CharField(max_length=32)
    rate = models.IntegerField()
    class Meta:
        db_table = 'article'

class Order(models.Model):
    id_user = models.ForeignKey("User", on_delete=models.CASCADE)
    id_article = models.ForeignKey("Article", on_delete=models.CASCADE)
    time = models.DateTimeField()
    class Meta:
        db_table = 'order'
