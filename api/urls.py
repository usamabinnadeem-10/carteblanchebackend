from django.urls import path, include
from .views import AddTodo, GetTodos

urlpatterns = [
    path('add-todo/', AddTodo.as_view()),
    path('get-todos/', GetTodos.as_view()),
]