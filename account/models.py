from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True )
    last_name = models.CharField(max_length=100, blank=True )
    phone = models.CharField(max_length=20,  blank=True, validators=[
        RegexValidator(regex=r"^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])")])

    def __str__(self):
        return f"{self.user}"
