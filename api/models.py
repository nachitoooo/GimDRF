from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)