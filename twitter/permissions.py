"""
Permissions for twitter.
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions for any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions for only owners.
        return obj.owner == request.user
