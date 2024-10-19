import django.urls
import rest_framework_simplejwt.views

import auth.views

app_name = "auth"


urlpatterns = [
    django.urls.path(
        "register/",
        auth.views.CreateUserView.as_view(),
        name="register",
    ),
    django.urls.path(
        "token/",
        rest_framework_simplejwt.views.TokenObtainPairView.as_view(),
        name="get_token",
    ),
    django.urls.path(
        "token/refresh/",
        rest_framework_simplejwt.views.TokenRefreshView.as_view(),
        name="refresh_token",
    ),
    # django.urls.path(
    #     "<int:pk>/",
    #     deck.views.DeckAPIDetail.as_view(),
    #     name="deck-detail",
    # ),
    # django.urls.path(
    #     "",
    #     deck.views.DeckViewSet.as_view({"get": "list"}),
    #     name="deck-list",
    # ),
    # django.urls.path(
    #     "<int:pk>/",
    #     deck.views.DeckViewSet.as_view({"put": "update"}),
    #     name="deck-detail",
    # ),
]
