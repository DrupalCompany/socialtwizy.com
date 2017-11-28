from django.apps import AppConfig


class FacebookparserConfig(AppConfig):
    name = 'facebookparser'
    verbose_name = 'Facebook Importer'

    def ready(self):
        from . import signals   # noqa