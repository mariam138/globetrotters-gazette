from django.shortcuts import render
# Allows use of built in generic views that Django supplies
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

    # display success message when user has registered
    messages.add_message(request, messages.SUCCESS, 'Registration successful!')


class PostsList(generic.ListView):
    # Displays posts which have been categorised in the USA/ Canada region
    queryset = Post.objects.filter(region='US')
    template_name = "posts_list.html"
