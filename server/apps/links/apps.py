from django.apps import AppConfig
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _


class LinksConfig(AppConfig):
    """Default configuration for Links app."""

    name = "apps.links"
    verbose_name = _("Links")

    def ready(self):
        """Set ID cursor for domains."""
        cache.get_or_set('domains-id', 0)
