from django.db import models

# Create your models here.
class Author(models.Model):
    Username = models.CharField(max_length=64, unique=True)
    Password = models.CharField(max_length=64)
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)

class Message(models.Model):
    Content = models.CharField(max_length=500)
    Date = models.DateField()
    Time = models.TimeField()
    Author = models.ForeignKey(Author, on_delete=models.PROTECT)