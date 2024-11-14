import django.urls
import justhink.routers
from django.conf import settings
from django.contrib import admin

import auth.urls
import lobby.urls
import lobby.views
import users.views

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
    django.urls.path(
        "lobby/",
        lobby.views.LobbyIdAPIView.as_view(),
        name="get-lobby-id",
    ),
    django.urls.path(
        "lobby/<str:uid>",
        lobby.views.LobbyAPIView.as_view(),
        name="lobby",
    ),
    django.urls.path(
        "users/<str:uid>",
        users.views.UserInfoView.as_view(),
        name="user-info",
    ),
    # django.urls.path("lobby/", django.urls.include(lobby.urls)),
    # django.urls.path("users/", django.urls.include(users.urls)),
]


if settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include("debug_toolbar.urls"),
        ),
    )
