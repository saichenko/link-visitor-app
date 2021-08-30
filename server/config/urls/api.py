from django.urls import include, path

app_name = "api"


urlpatterns = [
    # API URLS
    path("links/", include("apps.links.api.urls")),
]
