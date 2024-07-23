from django.db import models
# to create foreign key with django's User model
from django.contrib.auth.models import User

# Create your models here.

# Choice of regions for user's to set their blog post to
REGIONS = [
    ('AF', 'Africa'),
    ('AUS', 'Australasia'),
    ('EU', 'Europe / UK'),
    ('MENA', 'Middle East'),
    ('SA', 'South /Central America'),
    ('US', 'USA / Canada'),

]

# Will allow user to save their post as a draft
# Or upload it once published
STATUS = [
    ('0', 'Draft'),
    ('1', 'Published'),
]

class Post(models.Model):
    """
    Creates single instance of a Post model in relation to :model:`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    region = models.CharField(choices=REGIONS)
    country = models.CharField()
    slug = models.SlugField()
    body = models.TextField()
    status = models.CharField(choices=STATUS)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)