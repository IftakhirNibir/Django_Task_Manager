from django.contrib.auth import views as auth_views 
from django.urls import path 
from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path('task_creation/', views.task_creation, name="task_creation"),
    path('mylist/', views.mylist, name="mylist"),
    path('<int:task_id>/delete_task', views.confirm_delete_task, name='confirm_delete_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/update', views.task_update, name='task_update'),
    path('<int:task_id>/photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
]