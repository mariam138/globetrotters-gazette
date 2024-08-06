from django.db import models
from django_quill.fields import QuillField
from profile_page.models import Profile

# Create your models here.

class About(models.Model):
    """
    Creates single instance of an About model in relation to
    :model:`profile_page.Profile`
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="admin_profile")
    title = models.CharField(max_length=250)
    content = QuillField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def profile_picture(self):
        """
        Gets the profile picture from the Profile model rather than create
        a new field in the About model. This uses the @property decorator.
        Method adapted from:
        https://stackoverflow.com/questions/60987626/django-how-to-use-one-field-from-one-model-to-another-model
        """
        return self.profile.profile_picture