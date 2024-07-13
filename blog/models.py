from django.db import models
# takes information from User model in custom models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    birthday = models.DateField()
    bio = models.TextField()
    profile_pic = CloudinaryField('image')
    instagram = URLField()
    twitter_x = URLField()
    posts = ForeignKey(Post, on_delete=models.CASCADE)