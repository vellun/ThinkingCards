import rest_framework.serializers

import deck.models


class DeckSerializer(rest_framework.serializers.ModelSerializer):
    author = rest_framework.serializers.HiddenField(
        default=rest_framework.serializers.CurrentUserDefault()
    )

    class Meta:
        model = deck.models.Deck
        fields = (
            deck.models.Deck.name.field.name,
            deck.models.Deck.author.field.name,
            deck.models.Deck.is_public.field.name,
            deck.models.Deck.language.field.name, 
        )


__all__ = [DeckSerializer]
