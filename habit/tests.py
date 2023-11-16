from django.urls import reverse
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user.set_password('test_pass123')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Тестовое место',
            time='15:00:00',
            action='Тестовое действие',
            is_pleasant=False,
            period='1',
            reward='Тестовое вознаграждение',
            time_to_complete=85,
            is_public=True,
        )

    def test_habit_my_list(self):
        response = self.client.get(reverse('habits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'place': self.habit.place,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_pleasant': self.habit.is_pleasant,
                                     'foreign_habit': self.habit.foreign_habit,
                                     'reward': self.habit.reward,
                                     'time_to_complete': self.habit.time_to_complete,
                                 }
                             ]
                         })

    def test_habit_detail(self):
        response = self.client.get(reverse('habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'place': self.habit.place,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_pleasant': self.habit.is_pleasant,
                             'foreign_habit': self.habit.foreign_habit,
                             'period': self.habit.period,
                             'reward': self.habit.reward,
                             'time_to_complete': self.habit.time_to_complete,
                             'is_public': self.habit.is_public,
                         })

    def test_habit_create(self):
        data = {
            'owner': self.user,
            'place': 'Тестовое место 2',
            'time': '16:00:00',
            'action': 'Тестовое действие 2',
            'is_pleasant': True,
            'period': '5',
            'reward': '',
            'time_to_complete': 105,
            'is_public': True,
        }
        response = self.client.post(reverse('create_habit'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_validation(self):
        data = {
            'owner': self.user,
            'place': 'Тестовое место 3',
            'time': '17:00:00',
            'action': 'Тестовое действие 3',
            'is_pleasant': True,
            'period': '5',
            'reward': 'Вознаграждение',
            'time_to_complete': 105,
            'is_public': True,
        }
        response = self.client.post(reverse('create_habit'), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
                         {'Habit_validation_error': [
                             'Связанная привычка или вознаграждение не могут быть указаны в приятной привычке']})

    def test_habit_update(self):
        data = {
            'place': 'Тестовое место изменён',
            'time': '18:00:00',
            'action': 'Тестовое действие изменён',
            'is_pleasant': True,
            'period': '3',
            'time_to_complete': 15,
            'is_public': True,
        }
        response = self.client.put(reverse('update_habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'place': data['place'],
                             'time': data['time'],
                             'action': data['action'],
                             'is_pleasant': data['is_pleasant'],
                             'foreign_habit': self.habit.foreign_habit,
                             'period': data['period'],
                             'reward': self.habit.reward,
                             'time_to_complete': data['time_to_complete'],
                             'is_public': data['is_public'],
                         })

    def test_habit_destroy(self):
        response = self.client.delete(reverse('delete_habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)

    def test_all_habits(self):
        response = self.client.get(reverse('all_habits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{
                             'id': self.habit.id,
                             'place': self.habit.place,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_pleasant': self.habit.is_pleasant,
                             'foreign_habit': self.habit.foreign_habit,
                             'reward': self.habit.reward,
                             'time_to_complete': self.habit.time_to_complete,
                         }])
