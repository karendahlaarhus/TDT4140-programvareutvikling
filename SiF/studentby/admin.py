from django.contrib import admin

# Register your models here.

from .models import studentby
from kollektiv.models import kollektiv

class ChoiceInLine(admin.StackedInline):
    model = kollektiv
    extra = 3

class studentbyAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

admin.site.register(studentby, studentbyAdmin)
