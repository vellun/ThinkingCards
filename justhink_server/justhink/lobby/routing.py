from django.urls import path

import lobby.consumers

websocket_urlpatterns = [
    path("ws/<uid>/", lobby.consumers.LobbyConsumer.as_asgi()),
]