import rest_framework.generics
import rest_framework.viewsets
import rest_framework.decorators
from rest_framework import mixins

import core.models
import auth.serializers
import cards.permissions

import rest_framework.exceptions


class CreateUserView(rest_framework.generics.CreateAPIView):
    queryset = core.models.User.objects.all()
    serializer_class = auth.serializers.UserSerializer


__all__ = [CreateUserView]