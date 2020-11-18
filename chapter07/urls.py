from django.urls import path

from .views import index
from .views import dashboard
from .views import LoginView
from .views import LogoutView
from .views import RegisterView


app_name = "chapter07"

urlpatterns = [
    path('', index, name='index'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('users/register/', RegisterView.as_view(), name='register'),
    path('dashboard', dashboard, name='dashboard'),
]
