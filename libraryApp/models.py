from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    user_id = models.IntegerField(default=0)


class Book(models.Model):
    
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=60)
    genre = models.CharField(max_length=30)
    total_books = models.IntegerField(default=0)
    books_taken = models.IntegerField(default=0)
