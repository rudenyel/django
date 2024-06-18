from django.db import models
from django.contrib.auth.models import User
from project.enums import StatusTypes


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=StatusTypes.PUBLISHED)


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="+"
    )

    edited = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="+"
    )

    status = models.CharField(max_length=3,
                              choices=StatusTypes.choices,
                              default=StatusTypes.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        abstract = True
