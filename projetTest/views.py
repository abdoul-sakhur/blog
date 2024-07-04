from django.shortcuts import render,HttpResponse
# from django.views import View
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name="projetTest/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] ="Accueil du blog" 
        return context
    




def index(request):
    return  render(request,"projetTest/index.html")