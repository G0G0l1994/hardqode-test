from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""
    user_permissions = serializers.SlugRelatedField(slug_field='name',read_only = True,many=True)

    class Meta:
        model = User
        exclude = (
            'password',
            
            
        )


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
