from rest_framework import serializers

from users.models import User


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'avatar', 'telegram_id')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'city', 'avatar', 'telegram_id')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
