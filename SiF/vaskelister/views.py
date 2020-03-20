from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Task, Vaskeliste


def index(request, vaskeliste_id):
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    context = {'todo_list' : todo_list, 'vaskeliste_id' : vaskeliste_id}
    return render(request, 'todo/index.html', context)


def completeTodo(request):
    todo_liste = request.POST.getlist("task")
    task1 = Task.objects.get(pk=todo_liste[0])
    vaskeliste_id = task1.vaskeliste.id #bare for å få vaskelisten, tok første task men alle vil ha samme
    print(todo_liste)
    for todo_id in todo_liste:
        todo = Task.objects.get(pk=todo_id)
        checked = False
        if todo_id in request.POST: #dersom sjekkboksen er checked så vil den være submittet og derfor med i post-dictionarien
            checked = True
        if (not checked) and todo.complete:
            todo.complete = False
            todo.save()
        elif checked and (not todo.complete):
            todo.complete = True
            todo.save()
    url = 'http://127.0.0.1:8000/vask/' + str(vaskeliste_id)
    return redirect(url)



