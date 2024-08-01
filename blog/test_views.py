from django.test import TestCase

# Create your tests here.

class TestIndexView(TestCase):
    def test_index_returns_200_code(self):

        response = self.client.get('/')
        assert response.status_code == 200