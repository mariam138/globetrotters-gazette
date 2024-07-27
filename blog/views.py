from django.shortcuts import render
# Allows use of built in generic views that Django supplies
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    """
    Displays the index page as the home page

    ** Template **
        :template:`blog/index.html`
    """
    return render(request, 'blog/index.html')

    # display success message when user has registered
    messages.add_message(request, messages.SUCCESS, 'Registration successful!')


class AsiaPostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(region='ASIA')
    template_name = "post_list.html"
    paginate_by = 6
    context_object_name = "post_list"


class AfricaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='AF')

class AusPostList(AsiaPostList):
    queryset = Post.objects.filter(region='AUS')


class EuropePostList(AsiaPostList):
    queryset = Post.objects.filter(region='EU')


class MenaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='MENA')


class SAmericaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='SA')


class NAmericaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='US')


# Use of Django's generic Detail View to view each post in a separate view
class PostDetailView(detail.DetailView):
    model = Post
