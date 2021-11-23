""" This module contains the admin registration of todo_api"""
from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
