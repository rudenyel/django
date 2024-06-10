from django.db import models

from authors.models import Author
from project.mixins.models import BaseModel


class Book(BaseModel):
    # required fields
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=250)

    # optional fields with blank (or default) values
    finished = models.DateField(blank=True, null=True)

    authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='books',
        related_query_name='book'
    )

    def written_by(self):
        return ", ".join([author.surname for author in self.authors.all()])

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title
