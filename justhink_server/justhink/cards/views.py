import rest_framework.generics
import rest_framework.viewsets
import rest_framework.decorators
from rest_framework import mixins

import cards.models
import cards.serializers
import cards.permissions

import rest_framework.exceptions


class CardViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    rest_framework.viewsets.GenericViewSet,
):
    queryset = cards.models.Card.objects.all()
    serializer_class = cards.serializers.CardSerializer
    permission_classes = [cards.permissions.IsCardOwnerOrReadOnly]

    def perform_create(self, serializer):
        deck = serializer.validated_data["deck"]
        if not deck.author == self.request.user:
            raise rest_framework.exceptions.PermissionDenied(
                "You do not have permission to create a card in this deck."
            )
        serializer.save()


__all__ = [CardViewSet]
