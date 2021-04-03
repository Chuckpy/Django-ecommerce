from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True)
    
    
    def get_absolute_url(self):
        return reverse("/")
