import uuid
import asgiref
import channels
from rest_framework import views
from rest_framework import response
from rest_framework import exceptions
import django.core.cache


class LobbyIdAPIView(views.APIView):
    def get(self, request):
        uid = uuid.uuid4().hex

        django.core.cache.cache.set(
            f"lobby-{uid}", {request.user.username: "owner"}
        )

        return response.Response({"uuid": uid})


class LobbyAPIView(views.APIView):
    def get(self, request, uid):
        users = django.core.cache.cache.get(f"lobby-{uid}")

        if not users:
            raise exceptions.NotFound(
                detail="Lobby does not exist"
            )

        cur_user = request.user.username

        if cur_user not in users:
            channel_layer = channels.layers.get_channel_layer()
            asgiref.sync.async_to_sync(channel_layer.group_send)(
                f"lobby_{uid}",
                {
                    "type": "add_user",
                    "username": request.user.username,
                },
            )

        if not users.get(cur_user, None):
            users[cur_user] = "player"

            django.core.cache.cache.set(f"lobby-{uid}", users)

        return response.Response([users.keys()])
