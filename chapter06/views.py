from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
# flash message
from django.contrib import messages

from .models import Friend
from .forms import FriendForm

from .models import ClassRoom
from .models import Student
from .forms import ClassRoomForm
from .forms import StudentForm

from .models import Author
from .models import Category
from .models import Book
from .forms import AuthorForm
from .forms import CategoryForm
from .forms import BookForm

from .models import MonsterType
from .forms import MonsterTypeForm

from .models import Monster
from .forms import MonsterForm

# Create your views here.
def work01(request):
    params = {
        "title" : "work01",
#        "message" : "Hello, Work01",
    }
    return render(request, "chapter06/work01.html", params)


def friends_list(request):
    # 全件取り出し
    friends = Friend.objects.all()
    # 値の取り出し
    #friends = Friend.objects.all().values()
    # 特定のカラムの取り出し
    #friends = Friend.objects.all().values('id', 'name')
    # 件数
    #count = Friend.objects.all().count()
    #first = Friend.objects.all().first()
    #last = Friend.objects.all().last()
    # 検索
    """
    founds = Friend.objects.filter(name="ミッキー")
    founds = Friend.objects.filter(name__startwidth="ミ")
    founds = Friend.objects.filter(name__endwith="キ")
    founds = Friend.objects.filter(name__contains="ミ")
    founds = Friend.objects.filter(age=17)
    founds = Friend.objects.filter(age__gt=17)
    founds = Friend.objects.filter(age__gte=17)
    founds = Friend.objects.filter(age__lt=17)
    founds = Friend.objects.filter(age__lte=17)
    """
    
    params = {
        "title" : "友だち一覧",
#        "message" : "{}件のレコード".format(len(friends)),
        "friends" : friends
    }
    return render(request, "chapter06/friends/list.html", params)


def friends_view(request, id):
    friend = Friend.objects.get(id=id)
    params = {
        "title" : "友だち詳細表示",
#        "message" : "{}のデータ".format(friend.name),
        "friend" : friend
    }
    return render(request, "chapter06/friends/view.html", params)


def friends_edit(request, id):
    friend = Friend.objects.get(id=id)
    params = {
        "title" : "友だち編集",
#        "message" : "{}のデータ".format(friend.name),
        "friend" : FriendForm(instance=friend),
        "id" : friend.id,
    }
    if request.method == "POST":
        # POSTの代入
        friend_form = FriendForm(request.POST, instance=friend)
        # 更新
        friend_form.save()
        # リダイレクト
        return redirect("chapter06:friends_list")
    return render(request, "chapter06/friends/edit.html", params)


def friends_create(request):
    params = {
        "title" : "友だち新規作成",
#        "message" : "新規データ",
        "friend" : FriendForm,
    }
    if request.method == "POST":
        friend = Friend()
        friend_form= FriendForm(request.POST, instance=friend)
        friend_form.save()
        return redirect("chapter06:friends_list")
    return render(request, "chapter06/friends/create.html", params)

def friends_delete(request, id):
    friend = Friend.objects.get(id=id)
    friend.delete()
    return redirect("chapter06:friends_list")

def classrooms_list(request):
    classrooms = ClassRoom.objects.all()
    params = {
        "title" : "教室一覧",
        "classrooms" : classrooms,
    }
    return render(request, "chapter06/classrooms/list.html",params)

    
def classrooms_edit(request, id):
    classroom = ClassRoom.objects.get(id=id)
    params = {
        "title" : "教室編集",
        "classroom" : ClassRoomForm(instance=classroom),
        "id" : classroom.id
    }
    if request.method == "POST":
        # POSTの代入
        classroom_form = ClassRoomForm(request.POST, instance=classroom)
        # 更新
        classroom_form.save()
        # リダイレクト
        return redirect("chapter06:classrooms_list")
    return render(request, "chapter06/classrooms/edit.html",params)


def classrooms_create(request):
    params = {
        "title" : "教室作成",
        "classroom" : ClassRoomForm(),
    }
    if request.method == "POST":
        # POSTの代入
        classroom_form = ClassRoomForm(request.POST)
        # 更新
        classroom_form.save()
        # リダイレクト
        return redirect("chapter06:classrooms_list")
    return render(request, "chapter06/classrooms/create.html",params)


def students_list(request):
    students = Student.objects.all()
    params = {
        "title" : "生徒一覧",
        "students" : students,
    }
    return render(request, "chapter06/students/list.html",params)

    
def students_edit(request, id):
    student = Student.objects.get(id=id)
    params = {
        "title" : "生徒編集",
        "student" : StudentForm(instance=student),
        "id" : student.id
    }
    if request.method == "POST":
        # POSTの代入
        student_form = StudentForm(request.POST, instance=student)
        # 更新
        student_form.save()
        # リダイレクト
        return redirect("chapter06:students_list")
    return render(request, "chapter06/students/edit.html",params)


def students_create(request):
    params = {
        "title" : "生徒作成",
        "student" : StudentForm(),
    }
    if request.method == "POST":
        # POSTの代入
        student_form = StudentForm(request.POST)
        # 更新
        student_form.save()
        # リダイレクト
        return redirect("chapter06:students_list")
    return render(request, "chapter06/students/create.html",params)


def students_view(request, id):
    student = Student.objects.get(id=id)
    params = {
        "title" : "生徒表示",
        "form" : student,
    }
    return render(request, "chapter06/students/view.html",params)


from django.contrib.messages import get_messages

def authors_list(request):
    authors = Author.objects.all()
    params = {
        "title" : "著者一覧",
        "authors" : authors,
    }
    return render(request, "chapter06/authors/list.html", params)


def authors_edit(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author_form = AuthorForm(request.POST, instance=author)
        author_form.save()
        messages.success(request,"更新しました")
        return redirect("chapter06:authors_list")
    params = {
        "title" : "著者編集",
        "form" : AuthorForm(instance=author),
        "id" : author.id,
    }
    return render(request, "chapter06/authors/edit.html",params)


def authors_create(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        author_form.save()
        messages.success(request,"新規作成しました")
        return redirect("chapter06:authors_list")
    params = {
        "title" : "著者作成",
        "form" : AuthorForm(),
    }
    return render(request, "chapter06/authors/create.html",params)


def categories_list(request):
    categories = Category.objects.all()
    context = {
        "title" : "カテゴリ一覧",
        "categories" : categories,
    }
    return render(request, "chapter06/categories/list.html", context);


def categories_edit(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        category_form.save()
        messages.success(request, "更新しました")
        return redirect("chapter06:categories_list")
    context = {
        "title" : "カテゴリ編集",
        "form" : CategoryForm(instance=category),
        "id" : id,
    }
    return render(request, "chapter06/categories/edit.html",context)


def categories_create(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        category_form.save()
        messages.success(request, "新規カテゴリーを作成しました")
        return redirect("chapter06:categories_list")
    context = {
        "title" : "カテゴリ作成",
        "form" : CategoryForm()
    }
    return render(request, "chapter06/categories/create.html",context)


def books_list(request):
    books = Book.objects.all()
    context = {
        "title" : "本一覧",
        "books" : books,
    }
    return render(request, "chapter06/books/list.html",context)


def books_edit(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)
        book_form.save()
        messages.success(request, "本を更新しました")
        return redirect("chapter06:books_list")
    context = {
        "title" : "本の編集",
        "form" : BookForm(instance=book),
        "id" : id
    }
    return render(request, "chapter06/books/edit.html",context)


def books_create(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        book_form.save()
        messages.success(request, "本を作成しました")
        return redirect("chapter06:books_list")
    context = {
        "title" : "本の作成",
        "form" : BookForm(),
    }
    return render(request, "chapter06/books/create.html",context)


from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class MonsterTypeListView(ListView):
    # モデル名
    model = MonsterType
    # テンプレートファイル名のパス
    template_name = "chapter06/monster_type/list.html"
    # テンプレートファイルでのオブジェクト一覧の名前
    context_object_name = "monster_types"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスタータイプ一覧"
        return context


class MonsterTypeUpdateView(UpdateView):
    model = MonsterType
    form_class = MonsterTypeForm
    success_url = reverse_lazy("chapter06:monster_types_list")
    template_name = "chapter06/monster_type/edit.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスタータイプ新規作成"
        return context
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        return MonsterType.objects.get(id=pk)

class MonsterTypeCreateView(CreateView):
    # モデル名
    model = MonsterType
    # フィールド名
    #fields = ["name"]
    # フォームクラス名
    form_class = MonsterTypeForm
    # 成功時の遷移先URL指定
    success_url = reverse_lazy("chapter06:monster_types_list")
    # テンプレートファイル名の指定
    template_name = "chapter06/monster_type/create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスタータイプ編集"
        return context


class MonsterTypeDeleteView(DeleteView):
    # モデル名
    model = MonsterType
    # 成功時の遷移先URL指定
    success_url = reverse_lazy("chapter06:monster_types_list")

    def get(self, *args, **kwargs):
        # get primary key
        pk = self.kwargs.get("pk")
        # deleting object with pk
        MonsterType.objects.get(id=pk).delete()
        # redirect to success_url
        return redirect(self.success_url)


class MonsterTypeDetailView(DetailView):
    # モデル名
    model = MonsterType
    # テンプレートファイル名の指定
    template_name = "chapter06/monster_type/detail.html"
    # テンプレートでのオブジェクトの名前
    context_object_name = "monster_types"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスタータイプ表示"
        return context
    
    def get_object(self):
        pk = self.kwargs.get("pk")
        # get one
        #object = MonsterType.objects.get(id=pk)
        
        # get many _set.all()
        #for m in object.monster_set.all():
        #    print(m)
        
        # get fetche_related
        #mts =  MonsterType.objects.all().prefetch_related("monster_set").filter(id=pk)
        #for mt in mts:
        #    for m in mt.monster_set.all():
        #        print(m)
        
        mt =  MonsterType.objects.all().prefetch_related("monster_set").filter(id=pk).get()
        return mt

    
    """
    def get(self, *args, **kwargs):
        # get primary key
        pk = self.kwargs.get("pk")
        # deleting object with pk
        MonsterType.objects.get(id=pk).delete()
        # redirect to success_url
        return redirect(self.success_url)
    """
    

class MonsterListView(ListView):
    # モデル名
    model = Monster
    # テンプレートファイル名のパス
    template_name = "chapter06/monster/list.html"
    # テンプレートファイルでのオブジェクト一覧の名前
    context_object_name = "monsters"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスター一覧"
        return context
        
    def get_queryset(self):
        #monsters = Monster.objects.all()
        monsters = Monster.objects.all().select_related()
        return monsters


class MonsterCreateView(SuccessMessageMixin, CreateView):
    model = Monster
    form_class = MonsterForm
    template_name = "chapter06/monster/create.html"
    success_url = reverse_lazy("chapter06:monster_list")
    success_message = "新規作成しました"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスター作成"
        return context


class MonsterUpdateView(SuccessMessageMixin, UpdateView):
    model = Monster
    form_class = MonsterForm
    template_name = "chapter06/monster/edit.html"
    success_url = reverse_lazy("chapter06:monster_list")
    success_message ="更新しました"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "モンスター編集"
        return context


class MonsterDeleteView(SuccessMessageMixin, DeleteView):
    model = Monster
    success_url = reverse_lazy("chapter06:monster_list")
    
    def get(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        Monster.objects.get(id=pk).delete()
        messages.success(self.request, "削除しました")
        return redirect(self.success_url)

