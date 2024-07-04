from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.conf import settings
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200, null=True, blank=True)
    
    slug=models.SlugField()
    picture=models.ImageField(blank=True, upload_to='blog')

    class Meta:
        verbose_name="categorie"

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args, **kwargs)


class blogPost(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL, null=True)
    category=models.ForeignKey(Category,models.SET_NULL,null=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField()
    published=models.BooleanField(default=True)
    date=models.DateField(auto_created=True,blank=True,null=True)
    last_updated=models.DateTimeField(auto_now=True)
    content=models.TextField()
    description=models.TextField()
    picture=models.ImageField(blank=True, upload_to='blog')
# mode d'affichage dans la partie admin
    class Meta:
        ordering=["-date"]
        verbose_name="Article"

    def __str__(self):
        return self.title
    
    # creation de slug si le slug n'existe pas a partir du titre
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:index-app-blog")
class Message(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,models.SET_NULL,null=True)
    name=models.CharField(max_length=255, blank=True,null=True)
    surname=models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    description=models.TextField()

    def __str__(self):
        return self.name
    