from django.contrib import admin


from .models import Task, Vaskeliste
from kollektiv.models import kollektiv

class TaskInLine(admin.StackedInline):
    model = Task
    extra = 3

class vaskelisteAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [TaskInLine]

admin.site.register(Vaskeliste, vaskelisteAdmin)

