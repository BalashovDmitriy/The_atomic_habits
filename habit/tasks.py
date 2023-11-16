import datetime

from celery import shared_task
from django.utils import timezone

from habit.models import Habit


@shared_task
def habits_worker():
    habits = Habit.objects.all()
    for habit in habits:
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())
        now += datetime.timedelta(minutes=15)
        print(f"День привычки {habit.date.day}")
        print(f"Время привычки {habit.time.strftime('%H:%M')}")
        if (not habit.is_pleasant and
                now.hour == habit.time.hour and
                now.minute == habit.time.minute and
                now.day == habit.date.day):
            print(f"В {habit.time.strftime('%H:%M')} я буду {habit.action} в {habit.place}")
            if habit.foreign_habit:
                print("Сразу потом можно сделать:\n")
                print(habit.foreign_habit)
            elif habit.reward:
                print("Вознаграждение:\n")
                print(habit.reward)
            if habit.period == '1':
                habit.date += datetime.timedelta(days=1)
            elif habit.period == '2':
                habit.date += datetime.timedelta(days=2)
            elif habit.period == '3':
                habit.date += datetime.timedelta(days=3)
            elif habit.period == '4':
                habit.date += datetime.timedelta(days=4)
            elif habit.period == '5':
                habit.date += datetime.timedelta(days=5)
            elif habit.period == '6':
                habit.date += datetime.timedelta(days=6)
            elif habit.period == '7':
                habit.date += datetime.timedelta(days=7)
            habit.save()
