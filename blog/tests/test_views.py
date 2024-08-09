from django.test import TestCase, override_settings
import os
from unittest import mock

# # Create your tests here.
# @mock.patch.dict(os.environ, {"SECRET_KEY": "isw7=a3*siwii(_p24j3uu5d*a*yi%3wm*conti+gjv3)+(r!#"})
# @override_settings(
#     # SECRET_KEY=os.environ.get("SECRET_KEY"),
#     CLOUDINARY_STORAGE={
#         'CLOUD_NAME': 'your_cloud_name',
#         'API_KEY': 'your_api_key',
#         'API_SECRET': 'your_api_secret',
#     },
#     STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
# )
class TestIndexView(TestCase):
    def test_index_returns_200_code(self):
        # self.assertIsNotNone(os.environ.get('SECRET_KEY'))
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


# class TestAsiaPostList(TestCase):
#     def test_asia_post_list_view(self):
