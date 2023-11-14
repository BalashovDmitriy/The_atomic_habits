from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['place', 'time', 'action', 'is_pleasant', 'foreign_habit', 'period', 'reward',
                  'time_to_complete', 'is_public']


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['place', 'time', 'action', 'is_pleasant', 'foreign_habit', 'reward']
