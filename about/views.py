from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
# from django.views.generic.detail import DetailView
from .models import About
from blog.models import Post
from profile_page.models import Profile


def about_detail(request):
    """
    Displays a single instance of :model:`about.About`
    """

    # As admin was first user created, get admin by pk of 1
    admin = User.objects.get(id=1)
    # Orders all about objects from most recently updated
    # Then grabs the first instance only to be displayed
    about_detail = About.objects.all().order_by("-updated_on").first()

    # Create a queryset of all post objects that are published, approved
    # and written by the admin
    queryset = Post.objects.filter(status='1', approved=True, user=admin)
    # Create instance of post which gets the latest post admin has published
    post = queryset.order_by("-created_on").first()

    return render(
        request,
        "about/about.html",
        {"about_detail": about_detail,
         "post": post},
    )
