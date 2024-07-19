# Allows us to inherit from this class for our custom widget
from django.forms.widgets import ClearableFileInput

class CloudinaryFileInput(ClearableFileInput):
    pass