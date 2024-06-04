from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'phone', )
    ordering = ('id', )
