# pylint: disable=too-few-public-methods
""" Serializer Module for table ~booklist~ """
from rest_framework import serializers
from library.models import Booklist
from library.models import Users

class BooklistSerializer(serializers.ModelSerializer):
    """ Booklist Serializer class"""
    class Meta:
        """ Inner serializer class """
        model            = Booklist
        fields           = ['id', 'name', 'author', 'year', 'isbn', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class UsersSerializer(serializers.ModelSerializer):
    """ Users Serializer class"""
    class Meta:
        """ Inner serializer class """
        model            = Users
        fields           = ['id', 'name', 'email', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
