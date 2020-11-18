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
from .views import work01
from .views import friends_list
from .views import friends_view
from .views import friends_edit
from .views import friends_create
from .views import friends_delete

from .views import classrooms_list
from .views import classrooms_edit
from .views import classrooms_create

from .views import students_list
from .views import students_edit
from .views import students_create
from .views import students_view

from .views import authors_list
from .views import authors_edit
from .views import authors_create

from .views import categories_list
from .views import categories_edit
from .views import categories_create

from .views import books_list
from .views import books_edit
from .views import books_create

from .views import MonsterTypeListView
from .views import MonsterTypeUpdateView
from .views import MonsterTypeCreateView
from .views import MonsterTypeDeleteView
from .views import MonsterTypeDetailView

from .views import MonsterListView
from .views import MonsterUpdateView
from .views import MonsterCreateView
from .views import MonsterDeleteView

app_name = "chapter06"

urlpatterns = [
    path('work01', work01, name="work01"),
    path('friends/list', friends_list, name="friends_list"),
    path('friends/view/<int:id>', friends_view, name="friends_view"),
    path('friends/edit/<int:id>', friends_edit, name="friends_edit"),
    path('friends/create', friends_create, name="friends_create"),
    path('friends/delete/<int:id>', friends_delete, name="friends_delete"),
    path('classrooms/list', classrooms_list, name="classrooms_list"),
    path('classrooms/edit/<int:id>', classrooms_edit, name="classrooms_edit"),
    path('classrooms/create', classrooms_create, name="classrooms_create"),
    path('students/list', students_list, name="students_list"),
    path('students/edit/<int:id>', students_edit, name="students_edit"),
    path('students/create', students_create, name="students_create"),
    path('students/view/<int:id>', students_view, name="students_view"),

    path('authors/list', authors_list, name="authors_list"),
    path('authors/edit/<int:id>', authors_edit, name="authors_edit"),
    path('authors/create', authors_create, name="authors_create"),
    path('categories/list', categories_list, name="categories_list"),
    path('categories/edit/<int:id>', categories_edit, name="categories_edit"),
    path('categories/create', categories_create, name="categories_create"),

    path('books/list', books_list, name="books_list"),
    path('books/edit/<int:id>', books_edit, name="books_edit"),
    path('books/create', books_create, name="books_create"),

    path('monster_types/list', MonsterTypeListView.as_view(), name="monster_types_list"),
    path('monster_types/edit/<int:pk>', MonsterTypeUpdateView.as_view(), name="monster_types_edit"),
    path('monster_types/create', MonsterTypeCreateView.as_view(), name="monster_types_create"),
    path('monster_types/delete/<int:pk>', MonsterTypeDeleteView.as_view(), name="monster_types_delete"),
    path('monster_types/detail/<int:pk>', MonsterTypeDetailView.as_view(), name="monster_types_detail"),

    path('monster/list', MonsterListView.as_view(), name="monster_list"),
    path('monster/edit/<int:pk>', MonsterUpdateView.as_view(), name="monster_edit"),
    path('monster/create', MonsterCreateView.as_view(), name="monster_create"),
    path('monster/delete/<int:pk>', MonsterDeleteView.as_view(), name="monster_delete"),
]
