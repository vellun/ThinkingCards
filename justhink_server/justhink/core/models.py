import django.contrib.auth
import django.core.exceptions
import django.db.models


class User(django.contrib.auth.models.AbstractUser):
    username = django.db.models.CharField(
        verbose_name="никнейм",
        help_text="Придумайте уникальный никнейм",
        max_length=16,
        unique=True,
    )
    birthday = django.db.models.DateField(
        "дата рождения",
        help_text="Укажите дату рождения",
        null=True,
        blank=True,
    )
    friends = django.db.models.ManyToManyField(
        "self",
        blank=True,
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username
