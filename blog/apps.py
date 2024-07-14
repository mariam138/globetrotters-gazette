from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        """
        Overrides ready() from app config to register signals
        created for registration success message.
        """
        import blog.signals 
