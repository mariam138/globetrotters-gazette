from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

    # display success message when user has registered
    # messages.add_message(request, messages.SUCCESS, 'Registration successful!')