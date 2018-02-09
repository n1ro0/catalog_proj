from django.db import models


from . import querysets


class BaseManager(models.Manager):
    pass


ItemManager = BaseManager.from_queryset(querysets.ItemQuerySet)
