from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("tasks/",list_tasks, name= "tasks"),
    path("register",create_task,name="register"),
    path("edit/<int:id>",editTask,name="edit"),
    path("delete/<int:id>",destroyTask,name="delete"),
]
