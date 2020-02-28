from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task, Vaskeliste
from .forms import TodoForm

def index(request, vaskeliste_id):
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Task(text=request.POST['text'])
        new_todo.save()

    return redirect('http://127.0.0.1:8000/')

def completeTodo(request, todo_id):
    todo = Task.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('http://127.0.0.1:8000/')

def deleteCompleted(request):
    Task.objects.filter(complete__exact=True).delete()

    return redirect('http://127.0.0.1:8000/')

def deleteAll(request):
    Task.objects.all().delete()

    return redirect('http://127.0.0.1:8000/')
