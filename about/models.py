from django.db import models
from profile_page.models import Profile

# Create your models here.

class About(models.Model):
    """
    Creates single instance of an About model in relation to
    :model:`profile_page.Profile`
    """
    name = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="admin_name")
    profile_pic = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="admin_pic")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.name}