from django.db import models
from django.contrib.auth import models as auth_models


from . import signals
from catalog.core import models as core_models


class BaseUser(auth_models.AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created_at'
