from django.shortcuts import render,redirect
from .models import Task

# Create your views here
#   if request.method == 'POST':
 #       name = request.POST.get('name','')
 #       priority = request.POST.get('priority','')
 #       task = Task(name = name,priority = priority)
 #       task.save()
 #       return redirect('/')
 #   return render (request,'Myapp/add.html')


def index(request):
    task_list = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        task = Task(name = name,priority = priority)
        task.save()
        return redirect('/')




    return render(request,'Myapp/index.html',{'task_list':task_list})    


def delete(request,taskid):

    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'Myapp/delete.html',{'task':task})
