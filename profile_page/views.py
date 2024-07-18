from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

# decorator is used to ensure that only user's who are logged in
# can see this view. unauthorised users are redirected to login
# code from:
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator
@login_required
def profile_page(request):
    # try:
    #     # Get the profile for the logged-in user
    #     profile = Profile.objects.get(user=request.user)
    # # Handle case where profile does not exist
    # except Profile.DoesNotExist:
    #     profile = None

    # use the get_object_or_404 method to return a 404 page if profile is not found
    queryset = Profile.objects.get(user=request.user)
    profile = get_object_or_404(queryset)

    return render(request, 'profile_page/profile_page.html',
    {
        'profile': profile,
    },)
