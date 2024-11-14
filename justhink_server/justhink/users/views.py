from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import django.core.cache


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uid):
        username = request.user.username

        users = django.core.cache.cache.get(f"lobby-{uid}")

        if not users or not users.get(username, None):
            # TODO return error
            pass

        return Response(
            {
                "username": username,
                "role": users.get(username, None) if users else {},
            }
        )
