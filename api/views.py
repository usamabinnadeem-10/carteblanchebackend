from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

""" only accessed by authenticated users
    put, delete make sure that the requesting 
    user is the same as the one in database """
class AddTodo(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        data = request.data.copy()
        data['user'] = request.user.id
        serializer_todo = ToDoSerializer(data=data)

        if serializer_todo.is_valid():
            todo = serializer_todo.create(serializer_todo.validated_data)
            user_todos = Todo.objects.filter(user=request.user.id).order_by('-id')
            return Response(
                {
                    'todos' : ToDoSerializer(user_todos,many=True).data
                },status=status.HTTP_200_OK)
        else:
            return Response(
                serializer_todo.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        data = request.data.copy()
        obj = get_object_or_404(Todo, pk=data['id'])
        # Forbidden if user does not own this object
        if obj.user != request.user:
            return HttpResponseForbidden()

        data['user'] = request.user.id
        serializer_todo = ToDoSerializer(data=data)

        if serializer_todo.is_valid():
            Todo.objects.filter(pk=data['id']).update(**data)
            user_todos = Todo.objects.filter(user=request.user.id).order_by('-id')
            return Response(
                {
                    'todos' : ToDoSerializer(user_todos,many=True).data
                },
            status=status.HTTP_201_CREATED)
        return Response(serializer_todo.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):

        data = request.data.copy()
        obj = get_object_or_404(Todo, pk=data['id'])
        # Forbidden if user does not own this object
        if obj.user != request.user:
            return HttpResponseForbidden()

        obj.delete()
        user_todos = Todo.objects.filter(user=request.user.id).order_by('-id')
        return Response(
            {
                'todos' : ToDoSerializer(user_todos,many=True).data
            },status=status.HTTP_200_OK)


""" get all todos for the requesting user
    and sort them in descending order so 
    new todos are the latest  """
class GetTodos(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_todos = Todo.objects.filter(user=request.user.id).order_by('-id')

        return Response(
            {
                'todos' : ToDoSerializer(user_todos,many=True).data
            },
            status=status.HTTP_200_OK
        )

