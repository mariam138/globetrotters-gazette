# allows changing the input type for a field
from django import forms
# allows a form to be created from a preexisting model
from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
# import the Profile model to create the form
from .models import Profile


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
    profile_picture = CloudinaryFileField()

    class Meta:
        model = Profile
        # excludes the below fields in the form
        exclude = ["user", "created_on"]
        # customise widgets for profile form
        widgets = {
            # Allows a date picker for birthday instead of typing in manually
            "birthday": DateInput(),
        }

    # Apply cropping transformations to uploaded profile pic when uploaded
    # Code adapted from:
    # https://cloudinary.com/documentation/django_helper_methods_tutorial#adjust_the_code_forms_py_code_file
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].options = {
            'aspect_ratio': '1.0',
            'width': '250',
            'crop': 'fill',
            'gravity': 'faces',
            'fetch_format': 'webp',
        }
