from django.db import models
# takes information from User model in custom models
from django.contrib.auth.models import User
# uses cloudinary model to post images rather than django
from cloudinary.models import CloudinaryField
# import Post model from blog app
from blog.models import Post

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    birthday = models.DateField()
    bio = models.TextField()
    profile_pic = CloudinaryField('image')
    instagram = models.URLField()
    twitter_x = models.URLField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    # shows profiles made in descending order
    class Meta:
        ordering = ["-created_on"]