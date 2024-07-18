from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.

# decorator is used to ensure that only user's who are logged in
# can see this view. unauthorised users are redirected to login
# code from:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator
@login_required
def profile_page(request, username):
    """
    Displays an individual profile from :model:`profile_page.Profile`

    ** Context **

    ``profile``
        An instance of :model:`profile_page.Profile`

    ** Template **
        :template:`profile_page/profile_page.html`

    """

    # use the get_object_or_404 method to return a 404 page if profile is not found
    # using the lookup function via relationships -
    # going into the user field from the Profile model and searching for the username
    # code adapted from:
    # https://docs.djangoproject.com/en/4.2/topics/db/queries/#lookups-that-span-relationships
    profile = get_object_or_404(Profile, user__username=username)

    return render(request, 'profile_page/profile_page.html',
    {
        'profile': profile,
    },)
