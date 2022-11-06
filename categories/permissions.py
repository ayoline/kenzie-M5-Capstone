from rest_framework import permissions


class GetRouteOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            return request.user.is_superuser
