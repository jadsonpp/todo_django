from django.shortcuts import render,redirect
from .forms import taskForm
from .entity.entity import Task 
from .services.services import (
    registerTask,
    listTasks,
    listTaskId,
    deleteTask,
)
# Create your views here.
#List all tasks in the db.
def list_tasks(request):
    task = listTasks()
    return render(request,"tasks/list_task.html", {"tasks":task})

#Insert a new task
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
            newTask = Task(title,description,expiration_date,priority)
            #register the new task.
            
            return redirect ('tasks')
    form = taskForm()
    return render(request,"tasks/form_task.html",{"form":form})

def editTask(request,id):
    task = listTaskId(id)
    form = taskForm(request.POST or None, instance = task)
    if form.is_valid():        
        form.save()
        return redirect ('tasks')
    return render(request,"tasks/form_task.html",{"form":form})

def destroyTask(request,id):
    task = listTaskId(id)
    if request.method=="POST":
        deleteTask(task)
        return redirect ('tasks')
    return render(request,"tasks/confirm_delete.html",{'task':task})