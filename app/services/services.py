from ..models import Task

"""
    CRUD tasks
"""

#Register
def registerTask(task):
    Task.objects.create(title=task.title,description=task.description,
                        expiration_date=task.expiration_date,priority=task.priority)
    
#List all objetcs
def listTasks():
    #select * from app_task
    return Task.objects.all()

#select element by id
def listTaskId(id):
    return Task.objects.get(id=id)

#destroy
def deleteTask(task):
    task.delete()

