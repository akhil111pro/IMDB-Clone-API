from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        adimin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or adimin_permission
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user