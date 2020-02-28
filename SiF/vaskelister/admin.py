from django.contrib import admin


from .models import Task, Vaskeliste

class ChoiceInLine(admin.StackedInline):
    model = Task
    extra = 3

class vaskelisteAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    #search_fields = (Vaskeliste.__str__(self),) vil kunne søke på vaskelister etter tostringen, men fungerer ikke (ikke viktig)

admin.site.register(Vaskeliste, vaskelisteAdmin)

