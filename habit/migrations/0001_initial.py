# Generated by Django 4.2.7 on 2023-11-14 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=100, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('period', models.CharField(blank=True, choices=[('1', 'Раз в день'), ('2', 'Раз в два дня'), ('3', 'Раз в три дня'), ('4', 'Раз в четыре дня'), ('5', 'Раз в пять дней'), ('6', 'Раз в шесть дней'), ('7', 'Раз в семь дней')], default='1', null=True, verbose_name='Периодичность выполнения')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('time_to_complete', models.PositiveIntegerField(blank=True, null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('foreign_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit', verbose_name='Связанная привычка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
