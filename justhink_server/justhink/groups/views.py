import rest_framework.generics
import rest_framework.viewsets
import rest_framework.decorators
import rest_framework.permissions

import groups.models
import groups.serializers
import groups.permissions


class GroupViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = groups.models.Group.objects.all()
    serializer_class = groups.serializers.GroupSerializer
    permission_classes = [
        rest_framework.permissions.IsAuthenticated,
        groups.permissions.IsGroupParticipant,
    ]

    def get_queryset(self):
        return groups.models.Group.objects.filter(users=self.request.user)


__all__ = [GroupViewSet]
