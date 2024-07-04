from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
from django.http import HttpRequest
from compte.models import Client
from blog.models import blogPost ,Category,Message
from django.views.generic import ListView ,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth import get_user_model
from datetime import date
User=get_user_model()

# Create your views here.
class BlogPostIndexView(ListView): # type: ignore
    model=blogPost
    template_name="blog/index.html"
    context_object_name="posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories']=Category.objects.all()
         
                                                          
          category_id=self.kwargs.get('category_id')
          if category_id:
               context['categories']=blogPost.objects.filter(category_id=category_id)
          
          return context

         
def blog_by_category(request,id):
     posts=blogPost.objects.filter(category_id=id)
     categories=Category.objects.all()

     return render(request,'blog/blog_by_category.html',{'posts':posts,'categories':categories})

def create_post(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        published =request.POST.get('published')
        picture = request.FILES.get('picture')
        author = request.user
        category = Category.objects.get(id=category_id)

        post=blogPost.objects.create(
             title=title,
            content=content,
            description=description,
            category=category,
            published=published,
            picture=picture,
            author_id=author.id,
            date=date.today()
            )
            
        

        return redirect('posts:index')

    categories = Category.objects.all()
    return render(request, "blog/blog_form.html", context={"categories":categories})

 
class BlogPostUpdate(UpdateView):
     model= blogPost
     template_name= "blog/blog_form_edite.html"
     fields='__all__'
     context_object_name="post"
     success_url=reverse_lazy("posts:index")
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories']=Category.objects.all()
          return context
class BlogPostDetail(DetailView):
     model=blogPost
     template_name="blog/blog_detail.html"
     context_object_name="post"
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories']=Category.objects.all()
          return context
class BlogPostDelete(DeleteView):
     model=blogPost
     template_name="blog/blog_delete.html"
     context_object_name="post"
     success_url=reverse_lazy("posts:index")
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories']=Category.objects.all()
          
          return context
     

def message(request):
     if request.method =="POST":
         
          name=request.POST.get('name')
          surname=request.POST.get('surname')
          email=request.POST.get('email')
          description=request.POST.get('description')
          user_request=request.user
         
          message_creation = Message.objects.create( name=name, surname=surname, email=email, description=description,user_id=user_request.id)
          return redirect('posts:index')
     return render(request,'blog/index.html')

def apropos(request):
     categories=Category.objects.all()

     return render(request,'blog/apropos.html',context={'categories':categories})
