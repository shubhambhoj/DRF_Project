from rest_framework.permissions import BasePermission

class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET':
            return True
        return False
        
        # if request.method=='POST':
        #     return True
        # return False