from rest_framework import permissions


class IsGetOrIsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff and request.user.is_authenticated