from rest_framework import permissions


class IsOwnerOrIsAuthOnPatch(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "PATCH":
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and request.user.id == obj.id


class IsOwnerOrIsAuthOnCreate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and request.user.id == obj.id
