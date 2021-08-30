from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(
    r"visited-links",
    viewsets.VisitedLinksViewSet,
    basename="visited-links"
)
router.register(
    r"visited-domains",
    viewsets.VisitedDomainsViewSet,
    basename="visited-domains"
)
urlpatterns = router.urls
