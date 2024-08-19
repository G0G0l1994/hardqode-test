from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

from rest_framework import serializers

from users.models import Subscription,Balance

User = get_user_model()


class BalanceSerializer(serializers.ModelSerializer):
    """Сериализатор баланса"""

    def create(self, validated_data):
        return Balance.objects.create(**validated_data)
    
    class Meta:
        model = Balance
        fields = '__all__'
    


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""
    
        
    class Meta:
        model = User
        fields=['username','is_active','is_staff']

    def create(self, validated_data):
        new = User.objects.create(**validated_data)
        Balance.objects.create(users=new)
        
        return new


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    # TODO

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
            'active'
        )
