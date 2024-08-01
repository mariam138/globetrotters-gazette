# Allows a form to be created from existing model in db
from django.forms import ModelForm
# Import Summernote widgets
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget
# Import the Post model
from .models import Post


class PostForm(ModelForm):
    """
    Create form for user to create posts on client side
    """
    class Meta:
        model = Post
        # Excludes the below fields from the form
        exclude = ["user", "slug", "image_url", "approved", "created_on", "updated_on",]
        # Specify specific widgets
        widgets = {
            "body": SummernoteInplaceWidget(),
        }
