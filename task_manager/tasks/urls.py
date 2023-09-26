from django.contrib.auth import views as auth_views 
from django.urls import path 
from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
]