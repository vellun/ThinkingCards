from rest_framework import permissions


class IsCardOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.deck.is_public and request.method in permissions.SAFE_METHODS:
            return True

        return obj.deck.author == request.user
 