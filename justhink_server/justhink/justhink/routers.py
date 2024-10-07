from rest_framework import routers

import deck.views
import cards.views


deck_router = routers.SimpleRouter()
deck_router.register(r"decks", deck.views.DeckViewSet)

card_router = routers.SimpleRouter()
card_router.register(r"card", cards.views.CardViewSet)

