from django.db import models

# Create your models here.
class Author(models.Model):
    full_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name
    
class Book(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    book_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.book_name
        
