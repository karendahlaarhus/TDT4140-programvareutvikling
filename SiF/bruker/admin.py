from django.contrib import admin
from .models import bruker

class brukerAdmin(admin.ModelAdmin):
    fields = ['brukernavn', 'isManager']

admin.site.register(bruker, brukerAdmin)
