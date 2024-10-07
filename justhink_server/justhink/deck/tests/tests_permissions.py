import http
import itertools
from django.test import TestCase, Client
from django.contrib.auth.models import Permission
import django.urls
import parameterized.parameterized

import core.models
import deck.models


class PermissionsTests(TestCase):
    def setUp(self):
        self.deck_author = core.models.User.objects.create_user(
            username="user1", password="password"
        )
        self.not_deck_author = core.models.User.objects.create_user(
            username="user2", password="password"
        )

        self.test_public_deck = deck.models.Deck.objects.create(
            name="test_pub_deck", author=self.deck_author, is_public=True,
        )

        self.test_unpublic_deck = deck.models.Deck.objects.create(
            name="test_unpub_deck", author=self.deck_author, is_public=False,
        )

        self.client = Client()

    @parameterized.parameterized.expand(
        list(itertools.product(["user1", "user2"], [True, False], [http.HTTPStatus.OK]))
    )
    def test_get_deck_list(self, user, is_auth, status):
        if is_auth:
            self.client.login(username=user, password="password")

        response = self.client.get(django.urls.reverse("deck-list"))

        self.assertEqual(response.status_code, status)

    @parameterized.parameterized.expand(
        list(itertools.product(["user1", "user2"], [True, False], [http.HTTPStatus.OK]))
    )
    def test_get_deck_detail(self, user, is_auth, status):
        if is_auth:
            self.client.login(username=user, password="password")
        response = self.client.get(
            django.urls.reverse("deck-detail", args=["1"])
        )

        self.assertEqual(response.status_code, status)
