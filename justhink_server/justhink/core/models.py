from django.db import models
import django.contrib.auth


class User(django.contrib.auth.models.AbstractUser):
    shortname = django.db.models.CharField(
        verbose_name="имя",
        help_text="Введите свое имя(настояшее или вымышленное, \
            главное - чемпионское)",
        max_length=16,
        blank=True,
        null=True,
    )
    birthday = django.db.models.DateField(
        "дата рождения",
        help_text="Укажите дату рождения",
        null=True,
        blank=True,
        validators=[valid_birthday],
    )
    username = django.db.models.CharField(
        verbose_name="имя пользователя",
        help_text="Придумайте уникальное имя пользователя",
        max_length=16,
        unique=True,
    )
    image = django.db.models.ImageField(
        "аватарка",
        help_text="Загрузите аватарку",
        upload_to=get_path_image,
        null=True,
        blank=True,
    )
