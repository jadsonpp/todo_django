from django.contrib import admin
from django.urls import path
from .views.task import *
from .views.user import *

urlpatterns = [
    #CRUD Task
    path("tasks/",list_tasks, name= "tasks"),
    path("task_register",create_task,name="register"),
    path("edit/<int:id>",editTask,name="edit"),
    path("delete/<int:id>",destroyTask,name="delete"),
    #Register User
    path("user_register", register_user,name ='user_register'),
    #Login and logout
    path("login",login_user,name="login"),
    path("logout",logout_user,name="logout"),
]
