from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(
    r"visited-links",
    viewsets.VisitedLinksViewSet,
    basename="visited-links"
)
urlpatterns = router.urls
