from rest_framework import routers

import deck.views
import cards.views
import groups.views


deck_router = routers.SimpleRouter()
deck_router.register(r"decks", deck.views.DeckViewSet)

card_router = routers.SimpleRouter()
card_router.register(r"card", cards.views.CardViewSet)

group_router = routers.SimpleRouter()
group_router.register(r"groups", groups.views.GroupViewSet)
