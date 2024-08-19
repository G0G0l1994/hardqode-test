from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.response import Response


from api.v1.serializers.user_serializer import CustomUserSerializer, BalanceSerializer
from users.models import Balance

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Пользователи"""
    queryset = User.objects.all()
    serializer_class = [CustomUserSerializer]
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)


    def create(self,request):
        new = CustomUserSerializer(data=request.data)
        balance = Balance.objects.create(user_balance=new)
        new.save()
        balance.save()
        
        return Response({'post': new.data+balance.data,
                         },status=201,)
        

    
