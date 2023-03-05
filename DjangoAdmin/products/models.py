from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    likes = models.PositiveIntegerField(default=0)


"""
with this model we will get only the id of user 
"""


class User(models.Model):
    pass
