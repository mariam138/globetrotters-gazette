from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
import json

# Create your tests here.

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test1",
            password="testpassword",
            email="test@test.com"
        )
        self.post = Post(
            user = self.user,
            title = "Blog title",
            region = "AF",
            country = "Egypt",
            slug = "blog-title",
            image_url="",
            body=json.dumps({"delta": {"ops": [{"insert": "Hello, world!\n"}]}}),
            status='1',
            approved=True
        )
        self.post.save()

    def test_post_model_creation(self):
        """ Check post is an instance of the Post model"""
        self.assertTrue(isinstance(self.post, Post))
