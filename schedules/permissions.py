from rest_framework import permissions


class IsOwnerOrIsAuthOnGet(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_medic is not True:
            return True
        return (request.user.id == obj.medic.account.id) or (
            request.user.is_superuser
        )


class IsOwnerOrIsAuthOnPatch(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "PATCH":
            return request.user.is_authenticated
        else:
            if request.user.is_medic is not True:
                return True
            return (request.user.id == obj.medic.account.id) or (
                request.user.is_superuser
            )


class IsOwnerOrIsAuthOnCreate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return request.user.is_authenticated
        else:
            if request.user.is_medic is not True:
                return True
            return (request.user.id == obj.medic.account.id) or (
                request.user.is_superuser
            )


class IsMedicOwnerOrIsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.id == obj.medic.account.id) or (request.user.is_superuser)
