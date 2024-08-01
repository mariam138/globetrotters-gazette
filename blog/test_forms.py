from django.test import TestCase
from .forms import PostForm
# Create your tests here.

class TestPostForm(TestCase):
    """
    Includes tests on the :model:`blog.PostForm` model
    """
    def test_form_is_valid(self):
        post_form = PostForm({
            'title': 'Test Title',
            'region': 'SA',
            'country': 'Colombia',
            'body': 'This is a test form',
            'status': 0,
        })