from django.apps import AppConfig


class AstralprojappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'astralprojapp'

    def ready(self):
    	import astralprojapp.signals
