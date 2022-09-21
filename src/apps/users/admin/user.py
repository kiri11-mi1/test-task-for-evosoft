from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('login', 'is_superuser')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    )
