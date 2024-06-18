from django.db.models import IntegerChoices
from django.db import models


class StatusTypes(models.TextChoices):
    DRAFT = 'DRA', 'Draft'
    PUBLISHED = 'PUB', 'Published'
    DELETED = 'DEL', 'Deleted'


class RatingTypes(IntegerChoices):
    POOR = 1, 'Poor'
    FAIR = 2, 'Fair'
    GOOD = 3, 'Good'
    VERY_GOOD = 4, 'Very good'
    EXCELLENT = 5, 'Excellent'


