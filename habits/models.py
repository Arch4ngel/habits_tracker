from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}
PERIOD_CHOICES = [(1, 'Каждый день'),
                  (7, 'Каждую неделю'),
                  (28, 'Каждый месяц')]


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    location = models.CharField(max_length=50, verbose_name='Место')
    timing = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=50, verbose_name='Действие')
    nice = models.BooleanField(default=False, verbose_name='Приятность')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE, related_name='main_habit',
                                      verbose_name='Связанная привычка')
    period = models.PositiveIntegerField(default=1, choices=PERIOD_CHOICES, verbose_name='Периодичность')
    reward = models.CharField(max_length=50, verbose_name='Награда')
    duration = models.DurationField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
