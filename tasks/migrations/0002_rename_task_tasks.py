# Generated by Django 4.2.7 on 2023-12-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_task_user_fk'),
        ('tasks', '0001_task_user_fk'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tasks',
        ),
    ]
