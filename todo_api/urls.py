from . import views
from django.urls import path, include


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register_user'),

    # path('tasks/', views.CreateListTaskView.as_view({'get': 'list'}), name='create_task'),
    # path('tasks/<pk>' ,views.TaskUpdateDelete.as_view(),name='update_task'),
]
