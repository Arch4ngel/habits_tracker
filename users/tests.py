from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

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

    def test_user_create(self):
        """Тестирование создания пользователя"""

        response = self.client.post(
            '/users/user_create/',
            data={'id': 2, "email": 'test@sky.pro', "is_staff": "true", "is_active": "true", "is_superuser": "false",
                  "first_name": 'Petr', "last_name": 'Petrov', "telegram": 'telegram_test'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {'id': 2, "email": 'test@sky.pro', "is_staff": "true", "is_active": "true", "is_superuser": "false",
             "first_name": 'Petr', "last_name": 'Petrov', "telegram": 'telegram_test'}
        )

    def test_delete(self):

        response = self.client.delete(
            '/users/user_delete/2/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        data = {'id': 2, "email": 'test@sky.pro', "is_staff": "false", "is_active": "true", "is_superuser": "false",
                "first_name": 'Petr', "last_name": 'Petrov', "telegram": 'telegram_test'}

        response = self.client.put(
            '/users/user_update/2/',
            data=data
        )

        self.assertEquals(response.json(),
                          {'id': 2, "email": 'test@sky.pro', "is_staff": "false", "is_active": "true",
                           "is_superuser": "false",
                           "first_name": 'Petr', "last_name": 'Petrov', "telegram": 'telegram_test'}
                          )
