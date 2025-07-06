from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.contrib import messages


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
def task_list_view(request):
    tasks = Task.objects.all()
    
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    tasks = tasks.order_by('priority')
    
    return render(request, 'taskflowapp/task_list.html', {'tasks': tasks})
    
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        
        Task.objects.create(
            title = title,
            description = description,
            status = status,
            priority = priority,
            due_date = due_date
        )
        messages.success(request, 'Task created successfully!')
        return redirect('task_list_view')

    return render(request, 'taskflowapp/task_create.html')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.due_date = request.POST.get('due_date')
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('task_list_view')
    
    return render(request, 'taskflowapp/task_update.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == "POST":
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list_view')
    
    return render(request, 'taskflowapp/task_delete.html', {'task': task})




# Create your views here.
