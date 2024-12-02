import rest_framework.serializers

import groups.models


class GroupSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = groups.models.Group
        fields = (groups.models.Group.name.field.name,)

    def create(self, validated_data):
        user = self.context["request"].user
        group = groups.models.Group.objects.create(**validated_data)
        group.users.add(user)
        return group


__all__ = [GroupSerializer]
