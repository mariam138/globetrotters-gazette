# allows a form to be created from a preexisting model
from django.forms import ModelForm
# import the Profile model to create the form
from .models import Profile


class ProfileForm(ModelForm):
    """
    Create form for profile
    """
    class Meta:
        model = Profile
        # shows all fields except the created_on field
        exclude = ["user", "created_on"]
