from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# create signals to create a Profile instance automatically
# upon creating a User on registration
# code adapted from:
# https://dev.to/earthcomfy/django-user-profile-3hik
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, raw, **kwargs):
    if created and not raw:
        Profile.objects.create(
            user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, raw, **kwargs):
    if not raw:
        instance.profile.save()
