from django.shortcuts import render

from django.http import JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
import json
from django.views.decorators.http import require_POST
from rest_framework import generics

## restapi serializer
from .models import Todo
from .serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer




def todo_fetch(request):
    todos = Todo.objects.all()
    todo_list = []
    for index,todo in enumerate(todos, start=1):
        todo_list.append({'id':index, 'title':todo.title, 'completed':todo.completed})

    return JsonResponse(todo_list, safe=False)

@csrf_exempt
def todo_save(request):
    if request.body:
        data = json.loads(request.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                print('todo', todo)
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()
    return JsonResponse({})


def index(request):
    return render(request, 'todo/list.html')

