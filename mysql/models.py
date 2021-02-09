from django.db import models

class User(models.Model):
#    id_user = models.AutoField()
#    primary_key=True
    user_name = models.CharField(max_length=32)
    mail = models.EmailField()
    password = models.CharField(max_length = 32)
    adress = models.TextField()
# Create your models here.
