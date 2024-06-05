from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20,  blank=True)
    address = models.CharField(max_length=250, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"
