from django.contrib import admin

from project.mixins.admin import BaseAdmin
from authors.models import Author


@admin.register(Author)
class AuthorAdmin(BaseAdmin):
    list_display = ('id', 'surname', 'name', 'born', 'died', 'status')
    ordering = ('id', )
    prepopulated_fields = {'slug': ('name', 'surname'), }
