from rest_framework.permissions import IsAdminUser

class CustomPermission(IsAdminUser):
    """
    Custom permission class to check for admin permissions 
    """

    def has_permission(self, request, view):
        """
        function to allow only GET permission to normal user
        and CRUD to admin user
        """ 
        if request.method == 'GET':
            return request.user.is_authenticated
        else:
            return request.user.is_staff