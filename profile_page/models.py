from django.db import models
# takes information from User model in custom models
from django.contrib.auth.models import User
# Uses Quill fields for WYSIWYG editor
from django_quill.fields import QuillField
# uses cloudinary model to post images rather than django
from cloudinary.models import CloudinaryField
# import Post model from blog app
from blog.models import Post

# Create your models here.

class Profile(models.Model):
    """
    Stores an instance of a Profile related to :model:`auth.User`
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = CloudinaryField('image', blank=True)
    name = models.CharField(blank=True, max_length=250)
    birthday = models.DateField(null=True, blank=True)
    bio = QuillField(default="")
    instagram = models.URLField(blank=True)
    twitter_x = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    # Latest created profile will show first
    class Meta:
        ordering = ["-created_on"]

    # displays name|username for readability
    def __str__(self):
        return f"{self.name} | {self.user}"
