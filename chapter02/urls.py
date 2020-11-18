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

app_name = "chapter02"

urlpatterns = [
    path('work01', views.work01, name="work01"),
    path('work02a', views.work02a, name="work02a"),
    path('work02b', views.work02b, name="work02b"),
    path('work03a', views.work03a, name="work03a"),
    path('work03b', views.work03b, name="work03b"),
    path('work04a', views.work04a, name="work04a"),
    path('work04b', views.work04b, name="work04b"),
    path('work05a', views.work05a, name="work05a"),
    path('work05b', views.work05b, name="work05b"),
    path('work06', views.work06, name="work06"),
    path('work07', views.work07, name="work07"),
    path('work08', views.work08, name="work08"),
    path('work09', views.work09, name="work09"),
    path('work10', views.work10, name="work10"),
    path('work11', views.work11, name="work11"),
    path('work12', views.work12, name="work12"),
]
