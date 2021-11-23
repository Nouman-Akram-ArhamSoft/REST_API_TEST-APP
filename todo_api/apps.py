""" This module contains the app configuration of todo_api"""
from django.apps import AppConfig


class TodoApiConfig(AppConfig):
    """Class representing a Django application and its configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_api'
