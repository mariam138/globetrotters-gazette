from django.db import models


# Create your models here.

REGIONS = [
    ('AF', 'Africa'),
    ('AUS', 'Australasia'),
    ('EU', 'Europe / UK'),
    ('MENA', 'Middle East')
    ('SA', 'South /Central America'),
    ('US', 'USA / Canada'),

]

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    region = models.CharField(choices=REGIONS)
    country = models.CharField()
    slug = models.SlugField()
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)