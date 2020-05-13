from django.contrib import admin
from django.urls import path
from .views.task import *
from .views.user import *

urlpatterns = [
    #Login and logout
    path("",home,name="home"),
    path("login",login_user,name="login"),
    path("logout",logout_user,name="logout"),
    #CRUD Task
    path("tasks/",list_tasks, name= "tasks"),
    path("task_register",create_task,name="register"),
    path("edit/<int:id>",editTask,name="edit"),
    path("delete/<int:id>",destroyTask,name="delete"),
    #Register User
    path("user_register", register_user,name ='user_register'),
]
