import django.db.models

import deck.models


class Card(django.db.models.Model):
    text = django.db.models.CharField(
        verbose_name="текст",
        db_column="text",
        help_text="Введите понятие для карты",
        max_length=300,
    )

    deck = django.db.models.ForeignKey(
        deck.models.Deck,
        related_name="cards",
        on_delete=django.db.models.CASCADE,
    )

    class Meta:
        verbose_name = "карта"
        verbose_name_plural = "карты"

    def __str__(self):
        return self.text


__all__ = [Card]
