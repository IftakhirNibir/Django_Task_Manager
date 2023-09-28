from django.contrib import admin
from .models import *
from django.db.models import Case, When, IntegerField
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'priority', 'completed', 'user']
    list_filter = ['due_date', 'priority', 'completed']
    search_fields = ['title']
    date_hierarchy = 'due_date'
    ordering = (Case(
        When(priority='High', then=1),
        When(priority='Medium', then=2),
        When(priority='Low', then=3),
        default=4,
        output_field=IntegerField(),
    ),)

class TaskPhotoAdmin(admin.ModelAdmin):
    list_display = ['task', 'photo']

admin.site.register(Task,TaskAdmin)
admin.site.register(TaskPhoto,TaskPhotoAdmin)