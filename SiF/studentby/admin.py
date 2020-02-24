from django.contrib import admin

from .models import studentby
from kollektiv.models import kollektiv

admin.site.site_header = "SiF vaskelister adminside"
admin.site.site_title = "Adminside"
admin.site.site_index = "Side for administering av studentbyer og brukere"

class ChoiceInLine(admin.StackedInline):
    model = kollektiv
    extra = 3

class studentbyAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

admin.site.register(studentby, studentbyAdmin)
