from django.urls import include, path

urlpatterns = [
    path("api/v1/", include("config.urls.api", namespace="v1")),
]
