from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStudentOrReadOnly(BasePermission):
    message = "You are not a student"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_student
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.student == request.user