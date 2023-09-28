from django.contrib.auth import views as auth_views 
from django.urls import path, include 
from .views import *
from . import views
from .forms import LoginForm
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'taskphotos', views.TaskPhotoViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('task_creation/', TaskCreationView.as_view(), name='task_creation'),
    path('<int:task_id>/update', TaskUpdateView.as_view(), name='task_update'),
    path('<int:task_id>/delete_task', ConfirmDeleteTaskView.as_view(), name='confirm_delete_task'),
    path('<int:task_id>/photo/<int:photo_id>/delete/', DeletePhotoView.as_view(), name='delete_photo'),
    path('mylist/', MyListView.as_view(), name='mylist'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
    path('api/', include(router.urls)),
]