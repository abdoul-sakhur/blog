from django.urls import path
from django.contrib import admin
from compte.views import inscription,connexion,deconnexion,profile,update_profile

app_name="compte"
urlpatterns = [
    path('inscription/',inscription,name="inscription"),
    path('connexion/',connexion,name="connexion"),
    path('deconnexion/',deconnexion,name="deconnexion"),
  
    path('profile/<int:id>/',profile,name="profile"),
    path('update_profile/<int:id>/',update_profile,name="update_profile"),
   
    
]