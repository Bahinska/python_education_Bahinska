from django.apps import AppConfig


class ProductConfig(AppConfig):
    """
    Product application configuration class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
