from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
import datetime


from .models import Task, Vaskeliste
from .forms import TodoForm
from kollektiv.models import kollektiv
from studentby.models import studentby
from bruker.models import bruker as b


def index(request, vaskeliste_id):
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    current_week = int(datetime.datetime.now().strftime("%U"))+1
    if vaske_liste.week != current_week:
        for todo in todo_list:
            todo.complete = False
            todo.save()
        vaske_liste.week = current_week
        vaske_liste.save()
    context = {'todo_list' : todo_list, 'week': vaske_liste.week}
    return render(request, 'bruker/beboerside.html', context)

def completeTodo(request):
    todo_liste = request.POST.getlist("task")
    task1 = Task.objects.get(pk=todo_liste[0])
    vaskeliste_id = task1.vaskeliste.id #bare for å få vaskelisten, tok første task men alle vil ha samme
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


