from django.db import models

class Professor(models.Model):
    prof_id=models.CharField(max_length=10)
    prof_name=models.CharField(max_length=25)
    degree=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.prof_id
