from django.shortcuts import render
from kollektiv.models import kollektiv
from studentby.models import studentby


def index(request, studentby_id):
    studentby_list = studentby.objects.get(pk=studentby_id)
    kollektiv_list = kollektiv.objects.filter(studentby=studentby_list)
    context = {'kollektiv_list' : kollektiv_list, 'manager_for_by':studentby_list}
    return render(request, 'bruker/managerside.html', context)

