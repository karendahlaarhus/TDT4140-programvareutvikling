from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Task, Vaskeliste


def index(request, vaskeliste_id):
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    context = {'todo_list' : todo_list, 'vaskeliste_id' : vaskeliste_id}
    return render(request, 'todo/index.html', context)


def completeTodo(request):
    todo_liste = request.POST['task']
    print(todo_liste)
    for todo_id in todo_liste:
        todo = Task.objects.get(pk=todo_id)
        print(todo.text)
        vaskeliste_id = todo.vaskeliste.id
        if todo.complete:
            todo.complete = False
            todo.save()
            print("Endret til ikke complete")
        else:
            todo.complete = True
            todo.save()
            print("Endret til complete")
    url = 'http://127.0.0.1:8000/vask/' + str(vaskeliste_id)
    return redirect(url)



