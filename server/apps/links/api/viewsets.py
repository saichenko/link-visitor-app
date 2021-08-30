from django.core.cache import cache
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import VisitedLinksSerializer


class VisitedLinksViewSet(GenericViewSet, CreateModelMixin):
    """Creating visited links."""

    serializer_class = VisitedLinksSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """Create links and return Response with {'status': 'ok'} on success.
        Used to avoid returning created links in response.
        """
        super().create(request, *args, **kwargs)
        return Response({'status': 'ok'}, status=200)


class VisitedDomainsViewSet(GenericViewSet, ListModelMixin):
    """Listing visited domains."""

    def list(self, request, *args, **kwargs) -> Response:
        """Return Response with domains list.

        Query filtering params:
        `from` (int): `visited_at` greater.
        `to` (int): timestamp `visited_at` smaller.
        """
        param_from = request.GET.get('from')
        param_to = request.GET.get('to')

        domain_pks = map(
            lambda key: key.split(':')[1],
            cache.keys('domain:*:name')
        )

        domains = []
        for primary_key in domain_pks:
            name = cache.get(f'domain:{primary_key}:name')
            visited_at = cache.get(f'domain:{primary_key}:visited_at')
            domains.append((name, visited_at))

        if param_from:
            domains = filter(
                lambda domain: domain[1] > int(param_from),
                domains
            )

        if param_to:
            domains = filter(
                lambda domain: domain[1] < int(param_to),
                domains
            )

        return Response({'domains': domains, 'status': 'ok'}, status=200)
