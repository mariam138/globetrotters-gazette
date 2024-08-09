from django.test import TestCase
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from blog.models import Post, Comment
import json

# Create your tests here.

class TestModels(TestCase):
    def setUp(self):
        # Create title beforehand to test slugify
        title = "Blog title"
        #Code to parse correct json into body field adapted from:
        #https://github.com/LeeHanYeong/django-quill-editor/issues/69
        self.user = User.objects.create_superuser(
            username="test1",
            password="testpassword",
            email="test@test.com"
        )
        self.post = Post(
            user = self.user,
            title = title,
            region = "AF",
            country = "Egypt",
            slug = slugify(title),
            image_url="",
            body=json.dumps({"delta": {"ops": [{"insert": "Hello, world!\n"}]}}),
            status='1',
            approved=True
        )
        self.post.save()

        self.comment = Comment(
            user=self.user,
            post = self.post,
            body="This is a test comment",
            approved=True
        )
        self.comment.save()

    def test_post_model_creation(self):
        """ Check post is an instance of the Post model"""
        self.assertTrue(isinstance(self.post, Post))

    def test_post_str(self):
        """ Checks __str__ method of Post model"""
        self.assertEqual(str(self.post), "Blog title | User test1")

    def test_slug_creation(self):
        """ Checks slug is automatically created with slugify """
        self.assertEqual(self.post.slug, "blog-title")

    def test_comment_model_creation(self):
        """ Check comment is instance of Comment mode"""
        self.assertTrue(isinstance(self.comment, Comment))

    def test_comment_str(self):
        """ Check __str__ method of Comment model """
        self.assertEqual(str(self.comment), "This is a test comment")