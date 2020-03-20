from django.contrib import admin
from .models import bruker

class brukerAdmin(admin.ModelAdmin):
    fields = ['brukernavn', 'passord','isManager', 'kollektiv']
    list_filter = ('isManager', 'kollektiv')
    search_fields = ('brukernavn',)

admin.site.register(bruker, brukerAdmin)
