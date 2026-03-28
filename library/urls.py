from django.urls import path
from . import views

urlpatterns=[
    path('author/', views.AuthorView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('author/<int:id>', views.AuthorDetailView.as_view()),
    path('books/<int:id>', views.BookDetailView.as_view()),
]
