# Generated by Django 5.1.1 on 2024-11-16 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="friends",
            field=models.ManyToManyField(
                blank=True, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]