from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import Subscription, Balance
from courses.models import Course


def make_payment(request):
    # TODO
    balance = Balance.objects.get(request.user.id)
    price = Course.objects.get(request.data['course'])
    answer = balance - price
    if answer <= 0 and price.active == False:
        return False
    return True
    


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
            return True
        
        return False
        


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
