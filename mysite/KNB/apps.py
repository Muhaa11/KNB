from django.apps import AppConfig


class KnbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'KNB'

    def ready(self):
        import KNB.signals