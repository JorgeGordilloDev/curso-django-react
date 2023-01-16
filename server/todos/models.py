from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(
        "Nombre", max_length=50, help_text="Nombre de la lista de tareas"
    )
    description = models.CharField(
        "Descripción",
        blank=True,
        max_length=100,
        help_text="Descripción de la lista de tareas",
    )
    is_deleted = models.BooleanField("Eliminado", default=False)
    created_at = models.DateTimeField(
        "Fecha de creación", auto_now_add=True, auto_now=False
    )
    updated_at = models.DateTimeField(
        "Ultima modificación", auto_now_add=False, auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "TODO_LIST"
        verbose_name = "Lista de Tareas"
        verbose_name_plural = "Listas de Tareas"


class Todo(models.Model):
    title = models.CharField("Titulo", max_length=50, help_text="Titulo de la tarea")
    description = models.TextField("Descripción", help_text="Descripción de la tarea")
    is_completed = models.BooleanField("Completado", default=False)
    is_deleted = models.BooleanField("Eliminado", default=False)
    todo_list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, verbose_name="Lista de tareas"
    )
    created_at = models.DateTimeField(
        "Fecha de creación", auto_now_add=True, auto_now=False
    )
    updated_at = models.DateTimeField(
        "Ultima modificación", auto_now_add=False, auto_now=True
    )

    def __str__(self):
        return f"{self.title} - {self.todo_list.name}"

    class Meta:
        db_table = "TODO"
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
