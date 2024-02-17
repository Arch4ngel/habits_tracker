from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import *

appname = HabitsConfig.name

router_habits = routers.DefaultRouter()

router_habits.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [
    path('habits_public', PublicHabitAPIListView.as_view(), name='habits_public'),
] + router_habits.urls
