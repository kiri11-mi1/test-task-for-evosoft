from django.contrib import admin

from ..models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('diary__title',)
    search_fields = ('text',)
