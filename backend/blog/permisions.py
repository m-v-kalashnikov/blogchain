from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrAuthorCanEdit(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True

        is_author = request.user == obj.author

        return is_author


class AdminOrPostAuthorOrCommentAuthorCanDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser or request.user == obj.author:
            return True

        else:
            if request.method == 'DELETE' and request.user == obj.post.author:
                return True
            return False
