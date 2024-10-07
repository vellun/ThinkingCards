import django.contrib.admin

import core.models


@django.contrib.admin.register(core.models.User)
class UserAdmin(django.contrib.admin.ModelAdmin):
    list_display = (core.models.User.username.field.name,)


__all__ = []
