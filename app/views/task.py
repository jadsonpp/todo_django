from django.shortcuts import render,redirect
from ..forms import taskForm
from ..entity.entity import Task 
from ..services.services import (
    registerTask,
    listTasks,
    listTaskId,
    deleteTask,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

#List all tasks in the db.
@login_required
def list_tasks(request):
    task = listTasks(request.user)
    return render(request,"tasks/list_task.html", {"tasks":task})


#Insert a new task
@login_required
def create_task(request):
    if request.method == "POST":
        #take the datas
        form = taskForm(request.POST)
        #if the form contain the right datas.
        if form.is_valid():
            #Get and clean the datas from form.
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            expiration_date = form.cleaned_data['expiration_date']
            priority = form.cleaned_data['priority']
            #Pass the data into a class to work with object
            newTask = Task(title,description,expiration_date,priority,request.user)
            #register the new task.
            registerTask(newTask)
            return redirect ('tasks')
    form = taskForm()
    return render(request,"tasks/form_task.html",{"form":form})

@login_required
def editTask(request,id):
    task = listTaskId(id)
    if task.user != request.user: 
        return HttpResponse("Not your task!")
        
    form = taskForm(request.POST or None, instance = task)
    if form.is_valid():        
        form.save()
        return redirect ('tasks')
    return render(request,"tasks/form_task.html",{"form":form})

@login_required
def destroyTask(request,id):
    task = listTaskId(id)
    if task.user != request.user: 
        return HttpResponse("Not your task!")

    if request.method=="POST":
        deleteTask(task)
        return redirect ('tasks')
    return render(request,"tasks/confirm_delete.html",{'task':task})