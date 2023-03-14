from django.db import models
from passlib.hash import sha512_crypt as sha512

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    private_token = models.CharField(max_length=16,blank=True,null=True)

class Books(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100000)
    page_count = models.IntegerField()
    average_rating = models.FloatField()
    image_url = models.CharField(max_length=1000)
