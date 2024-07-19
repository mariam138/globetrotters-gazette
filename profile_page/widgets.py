# Allows us to inherit from this class for our custom widget
from django.forms.widgets import ClearableFileInput

class CloudinaryFileInput(ClearableFileInput):
    template_name = 'profile_page/cloudinary_file_input.html'

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        input_html = self._render(self.template_name, context, renderer)