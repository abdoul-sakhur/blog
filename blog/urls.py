from django.urls import path
from django.contrib import admin
from .views import ListView, BlogPostIndexView,create_post ,BlogPostUpdate,BlogPostDetail,BlogPostDelete,blog_by_category,message,apropos
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
app_name="posts"
urlpatterns = [
    path('',BlogPostIndexView.as_view(),name="index"),
    path('category/<str:id>',blog_by_category,name="category"),
    path('create/',login_required(create_post),name="create"),
    path('editer/<str:slug>/',login_required(BlogPostUpdate.as_view()),name="editer"),
    path('detail/<str:slug>/',BlogPostDetail.as_view(),name="detail"),
    path('delete/<str:slug>/',login_required(BlogPostDelete.as_view()),name="delete"),
    path('message',message,name="message"),
    path('apropos/',apropos,name="apropos")
    # path('category/<str:id>/', by_category, name='category'),
    
]
