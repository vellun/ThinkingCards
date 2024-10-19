import django.urls
import justhink.routers
from django.conf import settings
from django.contrib import admin

import auth.urls

API_PREFIX = "api/"

urlpatterns = [
    django.urls.path("admin/", admin.site.urls),
    django.urls.path(
        API_PREFIX, django.urls.include(justhink.routers.deck_router.urls)
    ),
    django.urls.path(
        API_PREFIX, django.urls.include(justhink.routers.card_router.urls)
    ),
    django.urls.path(API_PREFIX + "user/", django.urls.include(auth.urls)),
    # django.urls.path(API_PREFIX + "auth/", django.urls.include("rest_framework.urls")),
]


if settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include("debug_toolbar.urls"),
        ),
    )
