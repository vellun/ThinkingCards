import rest_framework.generics
import rest_framework.viewsets
import rest_framework.decorators
from rest_framework.response import Response
import rest_framework.permissions

import deck.models
import deck.serializers
from cards.serializers import CardSerializer
import deck.permissions


class DeckViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = deck.models.Deck.objects.all()
    serializer_class = deck.serializers.DeckSerializer
    permission_classes = [deck.permissions.IsDeckOwnerOrReadOnly]

    def get_permissions(self):
        print(self.request.user)
        if self.request.method not in rest_framework.permissions.SAFE_METHODS:
            self.permission_classes = [
                rest_framework.permissions.IsAuthenticated
            ]
        return super().get_permissions()

    @rest_framework.decorators.action(methods=["get"], detail=True)
    def cards(self, request, pk=None):
        deck = self.get_object()
        cards = deck.cards.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


__all__ = [DeckViewSet]
