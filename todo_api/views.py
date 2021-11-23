"""This module is used to create API for Todo_app"""
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, status
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .models import Task
from .serializers import CreateUserSerializer, TaskSerializer


# Create your views here.

class CreateListTaskView(viewsets.ModelViewSet):
    """
    ViewSet for CRUD API's
    """
    serializer_class = TaskSerializer
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        """
        Message: Create new task
        Parameters:
            request: Request from user for task creation
        Returns:
            Response:
        """
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user = valid_data['user_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=user)
        serializer.validated_data['person'] = user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self) -> Task:
        """
        queryset function to filter the specific task of user
        :return: Task
        """
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        tasks = Task.objects.filter(person=valid_data['user_id'])
        self.queryset = tasks
        return tasks


class RegisterUser(generics.CreateAPIView):
    """
    CreateAPIView for Registration of user
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, AdminRenderer]
