import django.urls

import lobby.views

app_name = "lobby"

urlpatterns = [
    django.urls.path(
        "",
        lobby.views.LobbyIdAPIView.as_view(),
        name="get-lobby-id",
    ),
    django.urls.path(
        "<str:uid>/",
        lobby.views.LobbyAPIView.as_view(),
        name="lobby",
    ),
]
