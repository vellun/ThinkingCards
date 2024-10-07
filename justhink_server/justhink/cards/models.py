from django.db import models


class Card(models.Model):
    text = models.CharField(
        verbose_name="текст",
        db_column="text",
        help_text="Введите понятие для карты",
        max_length=300,
    )
    
    deck = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "карта"
        verbose_name_plural = "карты"


__all__ = [Card]
