from rest_framework import permissions


class IsAdminOrAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_superuser
        else:
            return request.user.is_authenticated
