from django_celery_beat.models import IntervalSchedule, PeriodicTask


def create_periodic_send_reminder(habit, bot):
    text = (f'Привет, {habit.user}! Необходимо выполнять {habit.action} в {habit.timing} '
            f'в {habit.location} в течение {habit.duration}. Награда - {habit.reward}!')
    schedule, created = IntervalSchedule.objects.get_or_create(
         every=habit.period,
         period=IntervalSchedule.DAYS,
     )

    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Send reminder',
        task='habits.tasks.send_reminder',
        args=[habit.user.telegram, text],)
