from rest_framework import permissions


class IsOwnerOrIsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.method == "PATCH":
            return request.user.id == obj.id or request.user.is_superuser
        else:
            return request.user.is_superuser


class IsAuthOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        else:
            return request.user.is_superuser
