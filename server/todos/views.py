# https://www.django-rest-framework.org/api-guide/viewsets/
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *

# Create your views here.


class TodoListView(GenericViewSet):
    serializer_class = TodoListSerializer

    def get_queryset(self):
        return TodoList.objects.filter(is_deleted=False).order_by("-pk")

    def list(self, request):
        data = TodoList.objects.filter(is_deleted=False).order_by("-pk")
        serializer = TodoListSerializer(data, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=201,
            )

        return Response(
            {"error": "Error al crear el registro", "errors": serializer.errors},
            status=400,
        )

    def retrieve(self, request, pk=None):
        data = get_object_or_404(TodoList, pk=pk)
        serializer = TodoListSerializer(data)

        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(TodoList, pk=pk)
        serializer = TodoListSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro actualizado correctamente"})

        return Response(
            {
                "error": "Error al actualizar el registro",
                "errors": serializer.errors,
            },
            status=400,
        )

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(TodoList, pk=pk)
        serializer = TodoListSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro actualizado correctamente"})

        return Response(
            {
                "error": "Error al actualizar el registro",
                "errors": serializer.errors,
            },
            status=400,
        )

    def destroy(self, request, pk=None):
        obj = get_object_or_404(TodoList, pk=pk)
        obj.is_deleted = True
        obj.save()
        return Response({"message": "Registro eliminado correctamente"})

    @action(detail=True, methods=["GET"], url_path="todos", url_name="todos")
    def todos(self, request, pk=None):
        data = Todo.objects.filter(is_deleted=False, todo_list=pk)

        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)

    @action(
        detail=True, methods=["GET"], url_path="todos/deleted", url_name="todos/deleted"
    )
    def todos_deleted(self, request, pk=None):
        data = Todo.objects.filter(is_deleted=True, todo_list=pk)

        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="deleted", url_name="deleted")
    def deleted(self, request):
        data = TodoList.objects.filter(is_deleted=True)

        serializer = TodoListSerializer(data, many=True)
        return Response(serializer.data)


class TodoView(GenericViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(is_deleted=False).order_by("-pk")

    def list(self, request):
        data = Todo.objects.filter(is_deleted=False).order_by("-pk")
        serializer = TodoSerializer(data, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=201,
            )

        return Response(
            {"error": "Error al crear el registro", "errors": serializer.errors},
            status=400,
        )

    def retrieve(self, request, pk=None):
        data = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(data)

        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro actualizado correctamente"})

        return Response(
            {
                "error": "Error al actualizar el registro",
                "errors": serializer.errors,
            },
            status=400,
        )

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro actualizado correctamente"})

        return Response(
            {
                "error": "Error al actualizar el registro",
                "errors": serializer.errors,
            },
            status=400,
        )

    def destroy(self, request, pk=None):
        obj = get_object_or_404(Todo, pk=pk)
        obj.is_deleted = True
        obj.save()
        return Response({"message": "Registro eliminado correctamente"})

    @action(detail=False, methods=["GET"], url_path="deleted", url_name="deleted")
    def deleted(self, request):
        data = Todo.objects.filter(is_deleted=True)

        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)
