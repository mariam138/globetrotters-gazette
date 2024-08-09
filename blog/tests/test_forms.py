from django.test import TestCase
from blog.forms import PostForm, CommentForm
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


class TestCommentForm(TestCase):
    """
    Includes tests on the :model:`blog.CommentForm` model
    """
    def test_form_is_valid(self):
        comment_form = CommentForm({
            'body': "Test comment",
        })
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({
            'body': '',
        })
        self.assertFalse(comment_form.is_valid())