from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id', 'book_name', 'author']

class AuthorSerializer(serializers.ModelSerializer): # write parent later since it uses BookSerializer
    books=BookSerializer(many=True, read_only=True)
    class Meta:
        model=Author
        fields=['id', 'full_name', 'books']