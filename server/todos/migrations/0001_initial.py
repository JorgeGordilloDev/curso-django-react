# Generated by Django 4.1.5 on 2023-01-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de la lista de tareas', max_length=25, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, help_text='Descripción de la lista de tareas', verbose_name='Descripción')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Eliminado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
            ],
            options={
                'verbose_name': 'Lista de Tareas',
                'verbose_name_plural': 'Listas de Tareas',
                'db_table': 'TODO_LIST',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo de la tarea', max_length=25, verbose_name='Titulo')),
                ('description', models.TextField(help_text='Descripción de la tarea', verbose_name='Descripción')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Completado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima modificación')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.todolist', verbose_name='Lista de tareas')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'db_table': 'TODO',
            },
        ),
    ]
