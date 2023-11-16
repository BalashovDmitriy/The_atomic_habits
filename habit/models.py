from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    date = models.DateField(verbose_name='Дата, не заполнять', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    foreign_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.CharField(choices=[
        ('1', 'Раз в день'),
        ('2', 'Раз в два дня'),
        ('3', 'Раз в три дня'),
        ('4', 'Раз в четыре дня'),
        ('5', 'Раз в пять дней'),
        ('6', 'Раз в шесть дней'),
        ('7', 'Раз в семь дней'),
    ], default='1', verbose_name='Периодичность выполнения', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
