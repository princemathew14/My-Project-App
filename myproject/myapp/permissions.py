# myapp/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        # Allow access for all methods (view-level). Fine-grained check happens in has_object_permission.
        return True

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Deny write access if the object doesn't have an 'owner' attribute
        if not hasattr(obj, 'owner'):
            return False

        # Only allow the owner to edit/delete
        return obj.owner == request.user
