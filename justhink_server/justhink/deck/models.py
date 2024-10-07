from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Deck(models.Model):
    class Languages(models.TextChoices):
        RUSSIAN = "RU", _("Russian")
        ENGLISH = "EN", _("English")
        GERMAN = "DE", _("German")

    language = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.RUSSIAN,
    )

    name = models.CharField(
        verbose_name="название",
        db_column="name",
        help_text="Укажите название колоды",
        max_length=150,
    )

    is_public = models.BooleanField(
        verbose_name="публичная колода",
        db_column="is_public",
        default=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        db_column="created_on",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="decks",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "колода"
        verbose_name_plural = "колоды"


__all__ = [Deck]
