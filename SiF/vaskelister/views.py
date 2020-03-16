from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import datetime
from .models import Task, Vaskeliste
from .forms import TodoForm

def index(request: object, vaskeliste_id: object) -> object:
    week = datetime.datetime.now().strftime("%U")
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form, 'week' : week}
    return render(request, 'bruker/beboerside.html', context)


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
