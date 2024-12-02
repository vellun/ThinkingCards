import django.db.models

import core.models


class Group(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        help_text="Придумайте название",
        max_length=255,
        blank=True,
    )
    users = django.db.models.ManyToManyField(
        core.models.User,
        blank=True,
        related_name="user_groups",
    )
    created_at = django.db.models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name
