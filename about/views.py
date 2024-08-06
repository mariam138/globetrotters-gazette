from django.shortcuts import render, get_object_or_404
# from django.views.generic.detail import DetailView
from .models import About

def about_detail(request):
    """
    Displays a single instance of :model:`about.About`
    """
    # Orders all about objects from most recently updated
    # Then grabs the first instance only to be displayed
    about = About.objects.all().order_by("-updated_on").first()
    return render(
        request,
        "about/about.html",
        {"about":about},
    )