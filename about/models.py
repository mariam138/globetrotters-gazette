from django.db import models
from profile_page.models import Profile

# Create your models here.

class About(models.Model):
    """
    Creates single instance of an About model in relation to
    :model:`profile_page.Profile`
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="admin_profile")
    title = models.CharField(max_length=250)
    profile_pic = models.URLField(blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"