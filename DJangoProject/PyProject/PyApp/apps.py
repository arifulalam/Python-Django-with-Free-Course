from django.apps import AppConfig # type: ignore


class PyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PyApp'
