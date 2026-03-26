from django.shortcuts import render
from rest_framework import generics
from .models import Author as AuthorModel
from .models import Book as BookModel
from .serializers import AuthorSerializer, BookSerializer

class AuthorView(generics.ListCreateAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorSerializer

class BooksView(generics.ListCreateAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializer

class AuthorDetailView(generics.RetrieveUpdateDeleteAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorSerializer 
    lookup_field='id'   

class BookDetailView(generics.RetrieveUpdateDeleteAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializer 
    lookup_field='id'   