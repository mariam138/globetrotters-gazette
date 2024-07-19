# allows changing the input type for a field
from django import forms
# allows a form to be created from a preexisting model
from django.forms import ModelForm
# import the Profile model to create the form
from .models import Profile
# import the CloudinaryFileInput class to override the default widget
# from .widgets import CloudinaryFileInput
# from cloudinary.models import CloudinaryFileField

class DateInput(forms.DateInput):
    """
    Allows changing a form field in crispy forms to
    be a date picker rather than the standard text field.
    Code adapted from:
    https://forum.djangoproject.com/t/cant-change-type-attribute-in-django-crispy-forms/10054
    """
    input_type = "date"

class ProfileForm(ModelForm):
    """
    Create form for profile
    """
    class Meta:
        model = Profile
        # shows all fields except the created_on field
        exclude = ["user", "created_on"]
        # customise widgets for profile form
        widgets = {
            "birthday": DateInput(),
            # "profile_pic": CloudinaryFileInput()
        }
