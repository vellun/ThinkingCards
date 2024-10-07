import rest_framework.serializers

import cards.models


class CardSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = cards.models.Card
        fields = (
            cards.models.Card.text.field.name,
            cards.models.Card.deck.field.name,
        )


__all__ = [CardSerializer]
