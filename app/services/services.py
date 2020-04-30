from ..models import Task

"""
    CRUD tasks
"""

#Register
def registerTask(task):
    Task.objects.create(title=task.title,description=task.description,
                        expiration_date=task.expiration_date,priority=task.priority,user=task.user)
    
#List all objetcs
def listTasks(user):
    #select * from app_task
    return Task.objects.filter(user=user).all()

#select element by id
def listTaskId(id):
    return Task.objects.get(id=id)

#destroy
def deleteTask(task):
    task.delete()

