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


class AsiaPostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(region='ASIA')
    template_name = "post_list.html"
    paginate_by = 6
