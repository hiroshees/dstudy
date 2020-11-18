"""dpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "chapter04"

urlpatterns = [
    path('work01', views.work01, name="work01"),
    path('work02', views.work02, name="work02"),
    path('work03', views.work03, name="work03"),
    path('work04', views.work04, name="work04"),
    path('work05', views.work05, name="work05"),
    path('work06', views.work06, name="work06"),
    path('work07', views.work07, name="work07"),
    path('work08', views.work08, name="work08"),
    path('work09', views.work09, name="work09"),
]
