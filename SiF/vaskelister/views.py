from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Dette er begynnelsen på vaskelistesiden til SiF!")