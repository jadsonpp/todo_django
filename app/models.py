from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ("H", "High"),
        ("M","Medium"),
        ("L", "Low"),
    ]

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    expiration_date = models.DateField()
    priority = models.CharField(max_length=1,choices=PRIORITY_CHOICES)
    #
    user =models.ForeignKey(User, null=True,on_delete=models.CASCADE)



