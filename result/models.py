from django.db import models

class Result(models.Model):
    std_id=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
    marks=models.PositiveBigIntegerField()

    def __str__(self):
        return self.full_name
    
class MarkSheet(models.Model):
    std_name=models.ForeignKey(Result, on_delete=models.CASCADE, related_name='name')
    cgpa=models.FloatField()
    is_pass=models.BooleanField()

    def __str__(self):
        return str(self.std_name)