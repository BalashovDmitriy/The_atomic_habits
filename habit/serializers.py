from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ['id', 'place', 'time', 'action', 'is_pleasant', 'foreign_habit', 'period', 'reward',
                  'time_to_complete', 'is_public']

    def validate(self, data):
        """ Валидация привычки """
        # К полезной привычке нужно указать вознаграждение или приятную привычку
        if not data.get('foreign_habit') and not data.get('reward') and not data.get('is_pleasant'):
            raise serializers.ValidationError(
                {
                    'Habit_validation_error':
                        'К полезной привычке нужно указать вознаграждение или связанную привычку'}
            )
        # Исключить одновременный выбор связанной привычки и указания вознаграждения
        if data.get('foreign_habit') and data.get('reward'):
            raise serializers.ValidationError(
                {
                    'Habit_validation_error':
                        'Связанная привычка и вознаграждение не могут быть указаны вместе'}
            )
        # Время выполнения должно быть не больше 120 секунд
        if data.get('time_to_complete') > 120:
            raise serializers.ValidationError(
                {'Habit_validation_error': 'Время на выполнение не может быть больше чем 120 секунд'}
            )
        # В связанные привычки могут попадать только привычки с признаком приятной привычки
        if data.get('foreign_habit') and not data.get('foreign_habit').is_pleasant:
            raise serializers.ValidationError(
                {
                    'Habit_validation_error':
                        'Связанная привычка не может быть указана без признака приятной привычки'}
            )
        # У приятной привычки не может быть вознаграждения или связанной привычки.
        if data.get('is_pleasant') and data.get('foreign_habit') or data.get('is_pleasant') and data.get('reward'):
            raise serializers.ValidationError(
                {
                    'Habit_validation_error':
                        'Связанная привычка или вознаграждение не могут быть указаны в приятной привычке'}
            )
        return data


class HabitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'place', 'time', 'action', 'is_pleasant', 'foreign_habit', 'reward']
