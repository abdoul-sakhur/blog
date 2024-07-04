from typing import Any
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView ,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth import get_user_model,login,logout,authenticate
from compte.models import Profile,Client
from blog.models import Category
# Create your views here.
User=get_user_model()

def get_categories(request):
    categories=Category.objects.all()
    return render(request,'base.html',context={'categories':categories})

def inscription(request):
    categories=Category.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password != confirm_password :
            return HttpResponse('Le mot de passe ne correspond pas !')

        user=User.objects.create_user(
            username=username,
            password=password
        )
        login(request,user)
        return redirect('posts:index')
    return render(request,'inscription.html',context={'categories':categories})

def connexion(request):
    categories=Category.objects.all()
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:index')
    return render(request,'connexion.html',context={'categories':categories})



def deconnexion(request):
    logout(request)
    return redirect('posts:index')



def profile(request,id):
    categories=Category.objects.all()
    profile=Profile.objects.get(user_id=id)
    return render(request,'compte/profile.html',context={'profile':profile,'categories':categories})

def update_profile(request,id):
    categories=Category.objects.all()
    profile=Profile.objects.get(user_id=id)
    if request.method == "POST":
        bio=request.POST.get('bio')
        location=request.POST.get('location')
        picture=request.FILES.get('picture')
        if bio:
            profile.bio=bio
        if location:
            profile.location=location
        if picture:
            profile.picture=picture

        profile.save()
        return redirect('posts:index')
    return render(request,'compte/profile.html',context={'profile':profile,'categories':categories})