# Generated by Django 4.1 on 2022-09-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datam', '0003_alter_todo_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=300),
        ),
    ]
