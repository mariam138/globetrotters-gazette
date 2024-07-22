from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# allow use of the messages framework when updating profile
from django.contrib import messages
from django.urls import reverse
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


@login_required
def edit_save_profile(request, username):
    """
    Allows editing and saving of an individual profile from :model:`profile_page.Profile`

    ** Context **

    ``profile_form``
        An instance of :model:`forms.ProfileForm`

    ** Template **
        :template:`profile_page/edit_profile.html`

    """

    # create an instance of the profile model with logged in user's info
    profile = get_object_or_404(
        Profile, user__username=username)
    # load profile form, pre-populating fields that have already been filled by user
    profile_form = ProfileForm(instance=profile)

    # save profile edit to database
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and profile.user == request.user:
            # print(profile_form.profile_pic.url)
            profile.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your profile has been updated.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was a problem updating your profile. Please try again.'
            )

    return render(request, 'profile_page/edit_profile.html',
                  {
                      'profile_form': profile_form
                  })


@login_required
def edit_cancel_profile(request, username):
    """
    Allows cancelling and update of an individual profile from
    :model:`profile_page.Profile`.
    Displays message to user that changes were not saved if
    'Cancel' is pressed.

    ** Template **
        :template:`profile_page/edit_profile.html`

    """

    # create an instance of the profile model with logged in user's info
    profile = get_object_or_404(
        Profile, user__username=username)
    # load profile form, pre-populating fields that have already been filled by user
    profile_form = ProfileForm(instance=profile)
    # refreshes the instance with the last saved data from the database
    # code adapted from:
    # https://docs.djangoproject.com/en/4.2/ref/models/instances/#refreshing-objects-from-database
    profile.refresh_from_db()
    # Display message when changes were not saved
    messages.warning(
        request,
        'Your changes have not been saved.'
    )

    # if changes are cancelled, redirect user back to the profile page
    # code adapted from:
    # https://docs.djangoproject.com/en/4.2/ref/urlresolvers/#django.urls.reverse
    return HttpResponseRedirect(reverse('profile_page', args=[username]))
