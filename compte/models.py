from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import forms,Textarea
# Create your models here.
class Client(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    picture=models.ImageField(default="blog/profile.png", upload_to='blog')

    def __str__(self):
        return self.user.username
    
