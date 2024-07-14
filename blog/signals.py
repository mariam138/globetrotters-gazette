# allauth.account.signals.user_signed_up(request, user)
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_signed_up, user=User)
def reg_success_msg(request, user):
    messages.add_message(request, messages.SUCCESS, 'Registration successful!')
