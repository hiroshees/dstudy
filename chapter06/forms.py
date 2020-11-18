from django import forms
from .models import Friend
from .models import ClassRoom
from .models import Student
from .models import Author
from .models import Category
from .models import Book
from .models import MonsterType
from .models import Monster


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class FriendForm (forms.ModelForm):
    GENDER_CHOICES = (
        ("", "選択してください"),
        (1, "男"),
        (2, "女"),
    )
    
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
    
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    mail = forms.EmailField(label = "メール",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    gender = forms.ChoiceField(label="性別",
        choices = GENDER_CHOICES,
        widget=forms.Select(attrs={"class" : "form-control"}))
    age = forms.IntegerField(label = "年齢",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))
    birthday = forms.DateField(label = "誕生日",
        widget=forms.TextInput(attrs={"class" : "form-control", "type":"date"}))


class ClassRoomForm (forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['name']
    
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))


class StudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'class_room']

    name = forms.CharField(
        label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))

    age = forms.CharField(
        label = "年齢",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

    class_room = MyModelChoiceField(
        label="クラス",
        queryset=ClassRoom.objects.all(),
        widget=forms.Select(attrs={"class" : "form-control"}),
        empty_label=None)


class AuthorForm (forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
    
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))


class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))


class BookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'author', 'category',]

    title = forms.CharField(
        label = "タイトル",
        widget=forms.TextInput(attrs={"class" : "form-control"}))

    price = forms.CharField(
        label = "金額",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

    author = MyModelChoiceField(
        label="著者",
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={"class" : "form-control"}),
        empty_label="選択")

    category = MyModelChoiceField(
        label="カテゴリ",
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class" : "form-control"}),
        empty_label="選択")


class MonsterTypeForm (forms.ModelForm):
    class Meta:
        model = MonsterType
        fields = ['name']
    
    name = forms.CharField(label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))


class MonsterForm (forms.ModelForm):
    class Meta:
        model = Monster
        fields = ['name', 'hp', 'level', 'monster_type',]

    name = forms.CharField(
        label = "名前",
        widget=forms.TextInput(attrs={"class" : "form-control"}))

    hp = forms.IntegerField(
        label = "HP",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

    level = forms.IntegerField(
        label = "レベル",
        widget=forms.NumberInput(attrs={"class" : "form-control"}))

    monster_type = MyModelChoiceField(
        label="モンスター種類",
        queryset=MonsterType.objects.all(),
        widget=forms.Select(attrs={"class" : "form-control"}),
        empty_label="選択")
