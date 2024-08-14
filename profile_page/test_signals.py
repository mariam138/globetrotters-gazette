from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


# Create your tests here.
class TestProfileSignals(TestCase):
    """
    Test if the signals to create a Profile instance
    upon registering for the site is successful
    """
    def setUp(self):
        """
        Create a test instance of the :model:`auth.User`
        """
        self.user = User.objects.create_user(
            username="username1",
            email="username@user.com",
            password="MYpassword"
        )

    def test_profile_is_created(self):
        # Get profile object from self.user and check it exists
        profile = Profile.objects.get(user=self.user)
        self.assertTrue(profile)
