from django.contrib import admin

from project.mixins.admin import BaseAdmin
from books.models import Book, Category


@admin.register(Book)
class BookAdmin(BaseAdmin):
    list_display = ('id', 'title', 'written_by', 'category', 'finished', 'status')
    ordering = ('id', )
    prepopulated_fields = {'slug': ('title', ), }


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ('id', 'name', 'order', )
    ordering = ('id', )
    prepopulated_fields = {'slug': ('name', ), }
