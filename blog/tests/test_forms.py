from django.test import TestCase
from blog.forms import PostForm
import json
# Create your tests here.

class TestPostForm(TestCase):
    """
    Includes tests on the :model:`blog.PostForm` model
    """
    def test_form_is_valid(self):
        """ Tests form is valid """
        post_form = PostForm({
            'title': 'Test Title',
            'region': 'SA',
            'country': 'Colombia',
            'body': json.dumps({"delta": {"ops": [{"insert": "This is a test form\n"}]}}),
            'status': 0,
        })
        self.assertTrue(post_form.is_valid())

    def test_form_is_not_valid(self):
        post_form = PostForm({
            'title': '',
            'region': 'SA',
            'country': 'Colombia',
            'body': json.dumps({"delta": {"ops": [{"insert": "This is a test form\n"}]}}),
            'status': 0, 
        })
        self.assertFalse(post_form.is_valid())