import django.contrib

import cards.models


@django.contrib.admin.register(cards.models.Card)
class CardAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        cards.models.Card.text.field.name,
        cards.models.Card.deck.field.name,
    )


__all__ = []
