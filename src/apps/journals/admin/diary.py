from django.contrib import admin

from ..models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'expiration', 'user',)
    list_filter = ('kind', 'expiration',)
    search_fields = ('title', 'user',)
