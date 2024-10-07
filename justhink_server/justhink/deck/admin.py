import django.contrib

import deck.models


@django.contrib.admin.register(deck.models.Deck)
class DeckAdmin(django.contrib.admin.ModelAdmin):
    list_display = (deck.models.Deck.name.field.name,)


__all__ = []
