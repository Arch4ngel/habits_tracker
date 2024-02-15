from rest_framework.serializers import ValidationError
from datetime import timedelta


def habit_validator(value):

    max_time = timedelta(minutes=2)
    max_period = timedelta(days=7)

    try:
        if value['nice']:
            if value['related_habit'] or value['reward']:
                raise ValidationError('Приятная привичка не может иметь вознаграждения или связанной привычки')
    except KeyError:
        pass

    try:
        if value['related_habit'] and value['reward']:
            raise ValidationError('Выберите только приятную привычку или вознаграждение')
    except KeyError:
        pass

    try:
        if value['duration'] > max_time:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')
    except KeyError:
        pass

    try:
        if value['related_habit']:
            if not value['related_habit'].nice:
                raise ValidationError('В связанные привычки могут попадать только приятные привычки')
    except KeyError:
        pass

    try:
        if value['period']:
            if not timedelta(days=value['period']) > max_period:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
    except KeyError:
        pass
