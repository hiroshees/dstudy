# Generated by Django 3.1 on 2020-10-10 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapter06', '0004_classroom_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='classRoom',
            new_name='class_room',
        ),
    ]
