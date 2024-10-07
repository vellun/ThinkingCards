import pathlib
import uuid

import django.contrib.auth
import django.core.exceptions
import django.db.models


def get_path_image(instance, filename):
    file_extension = pathlib.Path(filename).suffix
    return f"users/{uuid.uuid4()}{file_extension}"


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
    # image = django.db.models.ImageField(
    #     "аватарка",
    #     help_text="Загрузите аватарку",
    #     upload_to=get_path_image,
    #     null=True,
    #     blank=True,
    # )
