import rest_framework.serializers

import core.models


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = core.models.User
        fields = (
            core.models.User.id.field.name,
            core.models.User.username.field.name,
            core.models.User.password.field.name,
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # user = core.models.User.objects.create(**validated_data)
        # return user

        user = core.models.User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user


__all__ = [UserSerializer]
