from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' ,'username', 'password' ]
        extra_kwargs = {'password': {'style': {'input_type':'password'}, 'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['task_title', 'task_description','is_complete', 'task_category',
                  'task_start_date', 'task_end_date']
