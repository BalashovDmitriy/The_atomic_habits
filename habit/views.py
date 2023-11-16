import datetime

from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habit.models import Habit
from habit.paginators import Paginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, HabitListSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone()) + datetime.timedelta(hours=1)
        habit = Habit.objects.get(pk=serializer.data['id'])
        if habit.time.hour > now.time().hour:
            habit.date = datetime.datetime.now().date()
            habit.save()
        elif habit.time.hour <= now.time().hour:
            habit.date = datetime.datetime.now().date() + datetime.timedelta(days=1)
            habit.save()
        print(habit.time.hour)
        print(now.time().hour)
        print(habit.date)
        # if self.request.data.get('time') < now.time():
        #     serializer.save(date=datetime.datetime.now().date())


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Paginator

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        pk = self.kwargs.get('pk')
        habit = Habit.objects.get(pk=pk)
        return super().get_object()


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Метод PATCH запрещён, используйте метод PUT"})


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class AllHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.all().filter(is_public=True)
