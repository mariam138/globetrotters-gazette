from django.shortcuts import render, get_object_or_404
# from django.views.generic.detail import DetailView
from .models import About

# Create your views here.
# class AboutDetailView(DetailView):
#     """
#     Uses Django's generic Detail view to display the About instance
#     """
#     model = About
#     template_name = "about/about.html"
#     context_object_name = "about"

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