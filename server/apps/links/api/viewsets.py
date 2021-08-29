from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import VisitedLinksSerializer


class VisitedLinksViewSet(GenericViewSet, CreateModelMixin):
    """ViewSet for creating visited links."""

    serializer_class = VisitedLinksSerializer
