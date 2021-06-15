from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsAuthorOrReadOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        condition = False
        if request.method in SAFE_METHODS:
            condition = True
        elif request.method in ("PUT", "POST", "UPDATE", "DELETE"):
            condition = request.user == obj
        
        return condition

class IsTargetPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.target