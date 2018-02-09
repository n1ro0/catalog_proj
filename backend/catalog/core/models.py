from django.db import models
from django.utils import timezone


from . import managers


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = managers.TimeStampedManager()

    class Meta:
        abstract = True
        get_latest_by = 'created_at'

