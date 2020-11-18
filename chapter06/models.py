from django.db import models

# Create your models here.
class Friend (models.Model):
    GENDER_CHOICES = (
        (1, '男'),
        (2, '女'),
    )
    
    name = models.CharField(
        max_length=100
    )
    mail = models.EmailField(
        max_length=200
    )
    gender = models.IntegerField(
        choices=GENDER_CHOICES
    )
    age = models.IntegerField(
        default=0
    )
    birthday = models.DateField(
    )
    
    def __str__(self):
        s = "<Friend " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name) + ">"
        return s


class ClassRoom (models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        s = "<ClassRoom " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name) + ">"
        return s


class Student (models.Model):
    name = models.CharField(
        max_length=100
    )
    age = models.IntegerField(
        default=0
    )
    class_room = models.ForeignKey(
        ClassRoom, 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        s = "<Student " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name) + "　" \
            "class_room.name=" + str(self.class_room.name) + ">"
        return s



class Category (models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        s = "Category " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name)
        return s


class Author (models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        s = "Autohr " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name)
        return s


class Book (models.Model):
    title = models.CharField(
        max_length=255
    )
    price = models.IntegerField(
        default=0
    )
    # ManyToOne
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    # ManyToOne
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        db_constraint=False,
    )

    def __str__(self):
        s = "Book " + \
            "id=" + str(self.id) + " " \
            "title=" + str(self.title) + "　" \
            "category.name=" + str(self.category.name) + "　" \
            "author.name=" + str(self.author.name)
        return s


class MonsterType (models.Model):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        s = "MonsterType " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name)
        return s


class Monster(models.Model):
    name = models.CharField(
        max_length=255
    )
    hp = models.IntegerField(
        default=0
    )
    level = models.IntegerField(
        default=0
    )
    # ManyToOne
    monster_type = models.ForeignKey(
        MonsterType,
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    
    def __str__(self):
        s = "MonsterType " + \
            "id=" + str(self.id) + " " \
            "name=" + str(self.name) + "　" \
            "monster_type.name=" + str(self.monster_type.name)
        return s

