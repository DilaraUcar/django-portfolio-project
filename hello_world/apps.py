from django.apps import AppConfig


class HelloWorldConfig(AppConfig):
    """
    Provides primary key type for hello_world app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello_world'
