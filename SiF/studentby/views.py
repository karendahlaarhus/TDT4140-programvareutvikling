from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from vaskelister.models import Task, Vaskeliste
from vaskelister.forms import TodoForm
from kollektiv.models import kollektiv
from studentby.models import studentby as st
from bruker.models import bruker

def index(request: object, studentby_id: object) -> object:
    studentby_list = st.objects.get(pk=studentby_id)
    kollektiv_list = kollektiv.objects.filter(studentby=studentby_list)
    correctVaskeliste = []
    for koll in kollektiv_list:
       vaskeliste = Vaskeliste.objects.filter(kollektiv=koll)
       correctVaskeliste.append(vaskeliste)
    form = TodoForm()
    context = {'text': "Hei", 'form' : form, 'kollektiv_list' : kollektiv_list, 'manager_for_by':studentby_list, 'correctVaskeliste':correctVaskeliste} #Får ikke til å peke på navn. Får bare opp databaseplasseringa
    return render(request, 'bruker/managerside.html', context)

