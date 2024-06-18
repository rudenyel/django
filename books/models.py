from django.db import models
from django.contrib.auth.models import User

from authors.models import Author
from project.mixins.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, blank=False)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Book(BaseModel):
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    finished = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='books', default='placeholder.jpg')

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True)

    authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='books',
    )

    favorites = models.ManyToManyField(
        User,
        blank=True,
        related_name='favorites',
    )

    def written_by(self):
        return ", ".join([author.surname for author in self.authors.all()])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
