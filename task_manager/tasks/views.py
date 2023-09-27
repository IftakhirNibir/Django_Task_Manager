from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    search_query = request.GET.get('search', '')
    creation_date_filter = request.GET.get('creation_date', '')
    due_date_filter = request.GET.get('due_date', '')
    priority_filter = request.GET.get('priority', '')
    completed_filter = request.GET.get('completed', '')

    tasks = Task.objects.all()

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if creation_date_filter:
        tasks = tasks.filter(created_at__date=creation_date_filter)

    if due_date_filter:
        tasks = tasks.filter(due_date=due_date_filter)

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    if completed_filter:
        tasks = tasks.filter(completed=completed_filter)

    return render(request, 'home.html', {
        'tasks': tasks,
        'search_query': search_query, 
        'creation_date_filter': creation_date_filter,
        'due_date_filter': due_date_filter,
        'priority_filter': priority_filter,
        'completed_filter': completed_filter,
    })

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {
        'form': form
    })


@login_required 
def task_creation(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            photos = request.FILES.getlist('photo')

             # Associate each photo with the task
            for photo in photos:
                TaskPhoto.objects.create(
                    task=task,
                    photo=photo,
                )

            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'task_creation.html', {
        'form': form,
        'title': 'Task Creation',
    })

def task_update(request, task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
  
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            form.save()
            photos = request.FILES.getlist('photo')

             # Associate each photo with the task
            for photo in photos:
                TaskPhoto.objects.create(
                    task=task,
                    photo=photo,
                )
            return redirect('.')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'task_update.html', {
        'form': form,
        'title': 'Task Update',
    })

def confirm_delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'confirm_delete_task.html', {'task': task})

def delete_photo(request, task_id, photo_id):
    task = get_object_or_404(Task, pk=task_id)
    photo = get_object_or_404(TaskPhoto, pk=photo_id, task=task)
    photo.delete()
    return redirect('task_detail', task_id=task_id)

   
def mylist(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'mylist.html', {'tasks': tasks})
    