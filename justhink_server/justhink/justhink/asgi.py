import os

import lobby.routing

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justhink.settings")

application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": URLRouter(lobby.routing.websocket_urlpatterns),
    },
)
