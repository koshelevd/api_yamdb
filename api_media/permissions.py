from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """Defines custom access permissions."""
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated and request.method == 'POST':
            return True
        if (request.method == 'PATCH'
                or request.method == 'DELETE') and (obj.author == request.user
                                                    or request.user.is_staff):
            return True
