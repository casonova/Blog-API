from rest_framework import permissions


class IsLoggedIn(permissions.BasePermission):
    """ Permission for Authenticated user """
    
    def has_permission(self, request, view,):
        return request.user and request.user.is_active
    
    def has_object_permission(self, request, view, obj):
        return  request.user and request.user.is_active


class IsAdminUser(permissions.BasePermission):
    """ Permission for Admin user """
    
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser