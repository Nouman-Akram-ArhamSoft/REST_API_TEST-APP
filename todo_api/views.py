from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from .models import Task
from .serializers import CreateUserSerializer, TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class CreateListTaskView(viewsets.ModelViewSet):

    serializer_class       = TaskSerializer
    permission_classes     = [IsAuthenticated]
    renderer_classes       = [JSONRenderer]
    authentication_classes = [JWTAuthentication]


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task_title = serializer.validated_data['task_title']
        task_description = serializer.validated_data['task_description']
        is_complete = serializer.validated_data['is_complete']
        task_category = serializer.validated_data['task_category']
        task_start_date = serializer.validated_data['task_start_date']
        task_end_date = serializer.validated_data['task_end_date']

        task_obj = Task(
            task_title=task_title, task_description=task_description, is_complete=is_complete,
            task_category=task_category, task_start_date=task_start_date, task_end_date=task_end_date
        )

        user = User.objects.filter(username=self.request.user)
        task_obj.person = user[0]
        task_obj.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def get_queryset(self):
        person = self.request.user
        person = User.objects.filter(username=person)
        if person:
            tasks = Task.objects.filter(person=person[0])
            self.queryset = tasks
            return tasks


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]
    renderer_classes   = [JSONRenderer, AdminRenderer]

