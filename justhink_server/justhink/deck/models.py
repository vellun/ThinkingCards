from django.db import models


class Deck(models.Model):
    name = models.CharField(
        verbose_name="название",
        db_column="name",
        help_text="Укажите название колоды",
        max_length=150,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        db_column="created_on",
    )
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "карта"
        verbose_name_plural = "карты"


__all__ = [Deck]
