from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from compte.models import Profile
from django.conf import settings

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile cree")

@receiver(post_save, sender=settings.AUTH_USER_MODEL) 
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        print("profile sauvegarde")