from django.contrib import admin

from project.mixins.admin import BaseAdmin
from books.models import Book


@admin.register(Book)
class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'author', 'finished', 'status')
    ordering = ('id', )
    prepopulated_fields = {'slug': ('title', ), }