from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    gender_cho = [("MAN","MAN"),("WOMAN","WOMAN")]
    gender = models.CharField(max_length=6, choices=gender_cho)
    
    def __str__(self):
        return self.username