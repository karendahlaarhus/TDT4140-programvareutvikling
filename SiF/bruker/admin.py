from django.contrib import admin
from .models import bruker

class brukerAdmin(admin.ModelAdmin):
    fields = ['brukernavn', 'passord','isManager', 'kollektiv', 'studentby']
    list_filter = ('isManager', 'kollektiv', 'studentby')
    search_fields = ('brukernavn',)

admin.site.register(bruker, brukerAdmin)
