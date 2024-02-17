from datetime import timedelta, time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@sky.pro',
            is_staff=True,
            is_active=True,
            is_superuser=False,
            first_name='Petr',
            last_name='Petrov',
            telegram='telegram_test'

        )
        self.user.set_password('12345')
        self.user.save()
        self.habit = Habit.objects.create(
            user=self.user,
            location='Gorod Testov',
            timing=time(10, 30, 0) ,
            action='Кроссфит',
            nice=True,
            related_habit=None,
            period=7,
            reward='Маленькая шоколадка',
            duration=timedelta(hours=1),
            is_public=False
        )

    def test_habit_create(self):
        response = self.client.post(
            '/habits/habit_create/',
            data={'pk': 2, "user": self.user.id, "location": "Gorod Testov", "timing": "10:30:00", "action": "Кроссфит",
                  "nice": True, "related_habit": None, "period": 7, "reward": "Маленькая шоколадка",
                  "duration": "01:00:00", "is_public": False}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'pk': 2, "user": self.user.id, "location": "Gorod Testov", "timing": "10:30:00", "action": "Кроссфит",
             "nice": 'true', "related_habit": 'null', "period": 7, "reward": "Маленькая шоколадка",
             "duration": "01:00:00", "is_public": 'false'}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_habit(self):

        response = self.client.get(
            '/habits/habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 2, 'next': None, 'previous': None, 'results': [{"user": self.user.id,
            "location": "Gorod Testov", "timing": "10:30:00", "action": "Кроссфит",
             "nice": 'true', "related_habit": 'null', "period": 7, "reward": "Маленькая шоколадка",
             "duration": "01:00:00", "is_public": 'false'}]})

    def test_delete(self):

        response = self.client.delete(
            '/habits/habit_delete/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        data = {'pk': 2, "user": self.user.id, "location": "Gorod Testov", "timing": "10:30:00", "action": "Кроссфит",
                "nice": 'true', "related_habit": 'null', "period": 1, "reward": "Маленькая шоколадка",
                "duration": "01:00:00", "is_public": 'true'}

        response = self.client.put(
            '/habits/habit_update/2/',
            data=data
        )

        self.assertEquals(response.json(),
                          {'pk': 2, "user": self.user.id, "location": "Gorod Testov", "timing": "10:30:00",
                           "action": "Кроссфит",
                           "nice": 'true', "related_habit": 'null', "period": 1, "reward": "Маленькая шоколадка",
                           "duration": "01:00:00", "is_public": 'true'}
                          )


def test_habit_public(self):

    response = self.client.get(
        '/habits/habits_public/'
    )

    self.assertEqual(
        response.status_code,
        status.HTTP_200_OK
    )

    self.assertEquals(
        response.json(),
        {'count': 2, 'next': None, 'previous': None, 'results': [{"user": self.user.id,
         "location": "Gorod Testov", "timing": "10:30:00", "action": "Кроссфит",
         "nice": 'true', "related_habit": 'null', "period": 7, "reward": "Маленькая шоколадка",
         "duration": "01:00:00", "is_public": 'true'}]})
