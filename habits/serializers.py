from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [habit_validator]
