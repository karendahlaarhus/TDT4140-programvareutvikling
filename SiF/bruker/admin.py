from django.contrib import admin
from .models import bruker

class brukerAdmin(admin.ModelAdmin):
    fields = ['brukernavn', 'isManager', 'kollektiv']
    list_filter = ('isManager', 'kollektiv')
    search_fields = ('navn',)

admin.site.register(bruker, brukerAdmin)
