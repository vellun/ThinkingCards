import uuid
from rest_framework import views
from rest_framework import response
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
            pass

        cur_user = request.user.username

        if not users.get(cur_user, None):
            users[cur_user] = "player"

            django.core.cache.cache.set(f"lobby-{uid}", users)

        return response.Response([users.keys()])
