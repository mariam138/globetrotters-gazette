from django.db import models
# to create foreign key with django's User model
from django.contrib.auth.models import User

# Create your models here.

# Choice of regions for user's to set their blog post to
REGIONS = [
    ('AF', 'Africa'),
    ('ASIA', 'Asia'),
    ('AUS', 'Australasia'),
    ('EU', 'Europe / UK'),
    ('MENA', 'Middle East'),
    ('SA', 'South / Central America'),
    ('US', 'USA / Canada'),

]

# Will allow user to save their post as a draft
# Or upload it once published
STATUS = [
    ('0', 'Draft'),
    ('1', 'Publish'),
]

class Post(models.Model):
    """
    Creates single instance of a Post model in relation to :model:`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(unique=True, max_length=250)
    region = models.CharField(choices=REGIONS, blank=True, max_length=100, default='')
    country = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    image_url = models.URLField(blank=True, default='')
    body = models.TextField()
    status = models.CharField(choices=STATUS, default='0', max_length=10)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        # Latest blog post shows first
        ordering = ["-created_on"]

    # Displays title|User(username) for readability
    def __str__(self):
        return f"{self.title} | User {self.user}"