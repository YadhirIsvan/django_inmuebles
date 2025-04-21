from rest_framework import permissions


class IsAdminOrReadOnly( permissions.IsAdminUser ):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        condicion = bool(request.user and request.user.is_staff)
        return condicion
    
class IsComentarioUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            return obj.user == request.user