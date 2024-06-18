from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from accounts.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def default_to_non_active(sender, instance, created, **kwargs):
#     if created:
#         instance.is_active = False
#         instance.save()
