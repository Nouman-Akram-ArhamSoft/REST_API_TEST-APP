"""this module is used to url management of todo_app"""
from django.urls import path
from . import views

APP_NAME = 'TODO_API'
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register_user'),
]
