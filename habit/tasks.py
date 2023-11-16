import datetime
from os import getenv

import requests
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
        if (not habit.is_pleasant and
                now.hour == habit.time.hour and
                now.minute == habit.time.minute and
                now.day == habit.date.day):
            message = (f"В {habit.time.strftime('%H:%M')} я буду {habit.action} в {habit.place}\n"
                       f"Время на выполнение: {habit.time_to_complete} секунд")
            send_message_to_telegram(message)
            if habit.foreign_habit:
                message = f"Сразу потом можно сделать:\n{habit.foreign_habit}"
                send_message_to_telegram(message)
            elif habit.reward:
                message = f"Вознаграждение за выполнение привычки:\n{habit.reward}"
                send_message_to_telegram(message)
            habit.date += datetime.timedelta(days=int(habit.period))
            habit.save()


def send_message_to_telegram(message):
    chat_id = getenv('TELEGRAM_CHAT_ID')
    bot_api_key = getenv('TELEGRAM_BOT_API_KEY')
    params = {'chat_id': chat_id, 'text': message}
    url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'
    requests.post(url, params=params)
