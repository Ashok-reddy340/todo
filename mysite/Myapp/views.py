from django.shortcuts import render
from .models import Task

# Create your views here
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        task = Task(name = name,priority = priority)
        task.save()
    return render (request,'Myapp/add.html')