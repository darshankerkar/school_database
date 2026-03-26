from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    admission_date=models.DateTimeField(auto_now_add=True)
    passout_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name