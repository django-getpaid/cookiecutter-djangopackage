from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class {{ cookiecutter.app_config_name }}(AppConfig):
    name = "{{ cookiecutter.app_name }}"
    verbose_name = _("{{ cookiecutter.broker_name }} backend")

    def ready(self):
        from getpaid.registry import registry

        registry.register(self.module)
