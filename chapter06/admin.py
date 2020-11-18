from django.contrib import admin
from .models import Friend
from .models import ClassRoom
from .models import Student
from .models import Book
from .models import Category
from .models import Author
from .models import Monster
from .models import MonsterType

admin.site.register(Friend)
admin.site.register(ClassRoom)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(MonsterType)
admin.site.register(Monster)
