from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return obj.creator == request.user


class IsAdminUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)