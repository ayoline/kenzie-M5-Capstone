from rest_framework import permissions


class IsOwnerOrIsAuthOnPatch(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method == "PATCH" or request.method == "DELETE":
            return request.user.is_authenticated and request.user.is_medic == False
        else:
            if request.user.is_authenticated:
                if request.user.is_medic:
                    if request.user.medics.id == obj.medic.id:
                        return True
                    return False
                return True
            return False
               

class IsOwnerOrIsAuthOnCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated and request.user.is_medic == False
        else:
            if request.user.is_authenticated:
                if request.user.is_medic:
                    if request.user.medics.id == int(view.kwargs["medic_id"]):
                        return True
                    return False
                return True
            return False
