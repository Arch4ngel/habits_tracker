from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits import services
from habits.models import Habit
from habits.paginations import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        services.create_periodic_send_reminder(new_habit)
        new_habit.save()


class PublicHabitAPIListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
