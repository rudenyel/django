from django.db import models
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=BaseModel.Status.PUBLISHED)


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

    class Status(models.TextChoices):
        DRAFT = 'DRA', 'Draft'
        PUBLISHED = 'PUB', 'Published'
        DELETED = 'DEL', 'Deleted'

    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        abstract = True
