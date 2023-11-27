""" Database Model Module """
from django.db import models

class Booklist(models.Model):
    """ Database table model for ~booklist~ """

    name   = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year   = models.IntegerField()
    isbn   = models.CharField(max_length=24)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    """ Database table model for ~users~ """
    name  = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
