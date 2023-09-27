from django.contrib import admin
from .models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'priority', 'completed', 'user']
    list_filter = ['due_date', 'priority', 'completed']
    search_fields = ['title']
    date_hierarchy = 'due_date'
    ordering = ['priority']  

class TaskPhotoAdmin(admin.ModelAdmin):
    list_display = ['task', 'photo']

admin.site.register(Task,TaskAdmin)
admin.site.register(TaskPhoto,TaskPhotoAdmin)