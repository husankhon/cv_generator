from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    degree = models.CharField()
    school = models.CharField()
    university = models.CharField()
    summary = models.TextField()
    previous_work = models.TextField()
    skills = models.CharField()
    