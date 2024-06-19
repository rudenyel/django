from django.db import models

from books.models import Book
from project.enums import RatingTypes
from project.mixins.models import BaseModel


class Review(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RatingTypes.choices, default=RatingTypes.EXCELLENT)
    title = models.CharField(max_length=250, blank=False)
    body = models.TextField(blank=False)

    class Meta:
        default_related_name = 'reviews'
        ordering = ('-created', 'title')


