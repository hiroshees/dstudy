"""dstudy URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapter02/', include('chapter02.urls')),
    path('chapter03/', include('chapter03.urls')),
    path('chapter04/', include('chapter04.urls')),
    path('chapter05/', include('chapter05.urls')),
    path('chapter06/', include('chapter06.urls')),
    path('chapter07/', include('chapter07.urls')),
#    path('chapter07/', include('django.contrib.auth.urls')),
    path('polls/', include('polls.urls')),
]


# django-debug-tookbar
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
