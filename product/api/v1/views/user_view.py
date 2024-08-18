from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.response import Response


from api.v1.serializers.user_serializer import CustomUserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Пользователи"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "head", "options"]
    permission_classes = (permissions.IsAdminUser,)
        
    # def get(self,request):
    #     queryset = User.objects.all()
    #     serializer_class = CustomUserSerializer(queryset,many=True)
    #     http_method_names = ["get", "head", "options"]
    #     permission_classes = (permissions.IsAdminUser,)
    #     return Response(serializer_class.data)

    
