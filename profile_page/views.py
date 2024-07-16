from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def profile_page(request):
    profile = Profile.objects.all()
    return render(request, 'profile_page/profile_page.html',
    {
        'profile': profile}
    