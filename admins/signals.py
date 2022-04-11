from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def set_usename(sender, *args, **kwargs):
    instance = kwargs['instance']
    if instance.email:
        instance.username = instance.email

