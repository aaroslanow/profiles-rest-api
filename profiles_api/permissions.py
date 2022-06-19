from rest_framework import permissions

class UpdateOwnProfile (permissions.BasePermission):
    """ allow user to update own profile"""
    def has_object_permission(self,request,view, obj):
        """Check User is trying to edit own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
        
