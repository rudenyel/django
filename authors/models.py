from django.db import models

from project.mixins.models import BaseModel


class Author(BaseModel):
    # required fields
    slug = models.SlugField(max_length=250, unique=True)
    surname = models.CharField(max_length=250)

    # optional fields with blank or default values
    name = models.CharField(max_length=250, blank=True)
    pen_name = models.CharField(max_length=250, blank=True)
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=250, blank=True)
    citizenship = models.CharField(max_length=250, blank=True)
    biography = models.TextField(blank=True)

    class Meta:
        ordering = ['surname']
        indexes = [
            models.Index(fields=['surname']),
        ]

    def __str__(self):
        return f"{self.name} {self.surname}" if self.name else self.surname
