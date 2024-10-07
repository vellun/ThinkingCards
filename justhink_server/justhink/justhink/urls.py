import django.urls
import justhink.routers
from django.conf import settings
from django.contrib import admin

API_PREFIX = "api/v1/"

urlpatterns = [
    django.urls.path("admin/", admin.site.urls),
    django.urls.path(
        API_PREFIX, django.urls.include(justhink.routers.deck_router.urls)
    ),
    django.urls.path(
        API_PREFIX, django.urls.include(justhink.routers.card_router.urls)
    ),
]


if settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include("debug_toolbar.urls"),
        ),
    )
