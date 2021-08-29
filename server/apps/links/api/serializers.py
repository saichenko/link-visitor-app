import typing

from django.core.cache import cache
from django.utils.timezone import datetime
from rest_framework import serializers
from tldextract import extract


def get_current_timestamp() -> int:
    """Return current timestamp with rounding."""
    return int(datetime.now().timestamp())


def extract_domains(urls: typing.Iterable) -> typing.Tuple[str]:
    """Return extracted domains from urls."""
    extracted_urls = map(extract, urls)
    domains = map(lambda url: url.registered_domain, extracted_urls)
    return tuple(domains)


class VisitedLinksSerializer(serializers.Serializer):
    """Serializer for creating visiting links."""

    links = serializers.ListField(
        child=serializers.CharField()
    )
    visited_at = serializers.HiddenField(
        default=get_current_timestamp
    )

    def create(self, validated_data: dict) -> dict:
        """Save domains to Redis.

        Saving patterns for links:
            `domain:<pk>:name`: Domain name. For example `google.com`.
            `domain:<pk>:visited_at`: Since epoch timestamp of visiting.
        """
        domains = extract_domains(validated_data['links'])
        for domain in domains:
            primary_key = cache.incr('domains-id')
            pattern = f'domain:{primary_key}:'
            cache.set_many({
                f'{pattern}name': domain,
                f'{pattern}visited_at': validated_data['visited_at']
            })
        return validated_data

    def update(self, instance, validated_data):
        """Escape warning."""
