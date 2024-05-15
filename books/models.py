from django.db import models

from authors.models import Author
from project.mixins.models import BaseModel


class Book(BaseModel):
    # required fields
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=250)

    # optional fields with blank (or default) values
    finished = models.DateField(blank=True, null=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='books'
    )

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return f"{self.title}"
