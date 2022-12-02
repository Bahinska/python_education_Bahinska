from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow admins of an object to edit it.
    Assumes the model instance has an `admin` attribute.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            if hasattr(request.user, "role"):
                return request.user.role == "admin"
            else:
                return False
        else:
            return False
