from django.apps import AppConfig


class ProfilePageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_page'

    def ready(self):
        """
        Overrides ready() from the app config to perform an initalisation
        task, which is registering the signals.
        Code adapted from:
        https://dev.to/earthcomfy/django-user-profile-3hik
        """
        import profile_page.signals  # noqa
