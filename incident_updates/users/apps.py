from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "incident_updates.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import incident_updates.users.signals  # noqa F401
        except ImportError:
            pass
