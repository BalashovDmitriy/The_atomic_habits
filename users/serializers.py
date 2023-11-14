from rest_framework import serializers

from habit.serializers import HabitSerializer
from users.models import User


class UserRetrieveSerializer(serializers.ModelSerializer):
    # habits = HabitSerializer(source='habits', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'avatar',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'city', 'avatar')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
