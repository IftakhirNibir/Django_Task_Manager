from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from rest_framework import viewsets
from .serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(View):
    def get(self, request):
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

class TaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, 'task_detail.html', {'task': task})

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'signup.html', {'form': form})

class TaskCreationView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_creation.html', {'form': form, 'title': 'Task Creation'})

    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            photos = request.FILES.getlist('photo')
            for photo in photos:
                TaskPhoto.objects.create(task=task, photo=photo)
            return redirect('home')

class TaskUpdateView(LoginRequiredMixin,View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskUpdateForm(instance=task)
        return render(request, 'task_update.html', {'form': form, 'title': 'Task Update'})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskUpdateForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            photos = request.FILES.getlist('photo')
            for photo in photos:
                TaskPhoto.objects.create(task=task, photo=photo)
            return redirect('task_detail', task_id=task_id)

class ConfirmDeleteTaskView(LoginRequiredMixin,View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'confirm_delete_task.html', {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('home')

class DeletePhotoView(LoginRequiredMixin,View):
    def get(self, request, task_id, photo_id):
        task = get_object_or_404(Task, pk=task_id)
        photo = get_object_or_404(TaskPhoto, pk=photo_id, task=task)
        photo.delete()
        return redirect('task_detail', task_id=task_id)

class MyListView(LoginRequiredMixin,View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'mylist.html', {'tasks': tasks})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskPhotoViewSet(viewsets.ModelViewSet):
    queryset = TaskPhoto.objects.all()
    serializer_class = TaskPhotoSerializer



    