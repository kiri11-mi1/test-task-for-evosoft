from django.contrib import admin

from ..models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ('text', 'diary',)
