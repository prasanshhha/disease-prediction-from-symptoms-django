from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class diseaseHistory(models.Model):
    diagnosis = models.CharField(max_length=200)
    date = models.DateField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)