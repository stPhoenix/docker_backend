from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsAuthorOrReadOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        condition = False
        if request.method in SAFE_METHODS:
            condition = True
        else:
            condition = request.user == obj.author
        
        return condition

class IsAuthorOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author