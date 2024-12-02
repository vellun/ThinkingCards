from rest_framework import permissions


class IsGroupParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.users.filter(id=request.user.id).exists()
