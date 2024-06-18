from django.contrib import admin

from project.mixins.admin import BaseAdmin
from reviews.models import Review


@admin.register(Review)
class AuthorAdmin(BaseAdmin):
    list_display = ('id', 'title', 'creator', 'created', 'rating', )
    ordering = ('-created', )
