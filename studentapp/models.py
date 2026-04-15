from django.db import models

# Create your models here.
class student(models.Model):
    roll= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    marks=models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.roll}"