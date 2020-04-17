from django.shortcuts import render, redirect
import datetime
from .models import Task, Vaskeliste


def index(request, vaskeliste_id):
    vaske_liste = Vaskeliste.objects.get(pk=vaskeliste_id)
    todo_list = Task.objects.filter(vaskeliste=vaske_liste)
    current_week = int(datetime.datetime.now().strftime("%U"))+1 #gir inneværende uke
    if vaske_liste.week != current_week: #dersom vaskelisten ikke er fra innværende uke, endre alle tasks til ikke gjort og endre vaskelistens uke til inneværende uke
        for todo in todo_list:
            todo.complete = False
            todo.save()
        vaske_liste.week = current_week
        vaske_liste.save()
    context = {'todo_list' : todo_list, 'week': vaske_liste.week}
    return render(request, 'bruker/beboerside.html', context)

def completeTodo(request):
    todo_liste = request.POST.getlist("task") #alle tasks som vises på siden
    task1 = Task.objects.get(pk=todo_liste[0])
    vaskeliste_id = task1.vaskeliste.id #for å få vaskelisten, tar første task men alle vil ha samme vaskeliste
    for todo_id in todo_liste:
        todo = Task.objects.get(pk=todo_id) #finner tilhørende task fra databasen
        checked = False
        if todo_id in request.POST: #dersom sjekkboksen er checked så vil den være submittet og derfor med i post-dictionarien
            checked = True
        if (not checked) and todo.complete: #dersom sjekkboksen ikke er sjekket av og Task i databasen er complete, endre Task til ikke complete
            todo.complete = False
            todo.save()
        elif checked and (not todo.complete): #dersom sjekkboksen er sjekket av og Task i databasen ikke er complete, endre Task til complete
            todo.complete = True
            todo.save()
    url = 'http://127.0.0.1:8000/vask/' + str(vaskeliste_id)
    return redirect(url)


