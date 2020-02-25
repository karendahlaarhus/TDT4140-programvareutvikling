from django.contrib import admin

import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from django.contrib.sites.models import Site

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.unregister(Site)

from .models import studentby
from kollektiv.models import kollektiv

admin.site.site_header = "SiF vaskelister adminside"
admin.site.site_title = "Adminside"
admin.site.index_title = "Side for administering av studentbyer og brukere"

class ChoiceInLine(admin.StackedInline):
    model = kollektiv
    extra = 3

class studentbyAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    search_fields = ('navn',)

admin.site.register(studentby, studentbyAdmin)

