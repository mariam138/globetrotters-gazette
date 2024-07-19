# # Allows us to inherit from this class for our custom widget
# from django.forms.widgets import ClearableFileInput
# # Renders the custom HTML without further escaping
# # Adapted from: https://docs.djangoproject.com/en/4.2/ref/utils/#django.utils.safestring.mark_safe
# from django.utils.safestring import mark_safe


# class CloudinaryFileInput(ClearableFileInput):
#     template_name = 'profile_page/cloudinary_file_input.html'

#     # Use get_context method to hide the default widget
#     # Code adapted from: https://www.reddit.com/r/django/comments/d3jjg6/how_in_the_world_do_i_customize_djangos/
#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)

#         context['widget']['is_hidden'] = True

#         return context

#     def render(self, name, value, attrs=None, renderer=None):
#         """Render the widget as an HTML string."""
#         context = self.get_context(name, value, attrs)
#         input_html = self._render(self.template_name, context, renderer)

#         # Define html for custom widget
#         # Overrides default 'file' input behaviour so that
#         # Cloudinary widget opens first instead
#         cloudinary_btn_html = (
#             '<button type="submit" class="btn btn-primary" id="upload_widget_btn">'
#             'Choose file</button>'
#         )

#         # Combine the custom HTML with the input HTML
#         return mark_safe(f'{input_html}{cloudinary_btn_html}')
