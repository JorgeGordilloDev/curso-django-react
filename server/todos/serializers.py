from rest_framework.serializers import ModelSerializer
from .models import *


class TodoListSerializer(ModelSerializer):
    def to_representation(self, instance: TodoList):
        return {
            "id": instance.pk,
            "name": instance.name,
            "description": instance.description,
            "is_deleted": instance.is_deleted,
            "created_at": instance.created_at.strftime("%D %H:%S"),
            "updated_at": instance.updated_at.strftime("%D %H:%S"),
        }

    class Meta:
        model = TodoList
        fields = "__all__"


class TodoSerializer(ModelSerializer):
    def to_representation(self, instance: TodoList):
        return {
            "id": instance.pk,
            "title": instance.title,
            "description": instance.description,
            "is_complete": instance.is_completed,
            "is_deleted": instance.is_deleted,
            "todo_list": instance.todo_list.pk,
            "created_at": instance.created_at.strftime("%D %H:%S"),
            "updated_at": instance.updated_at.strftime("%D %H:%S"),
        }

    class Meta:
        model = Todo
        fields = "__all__"
