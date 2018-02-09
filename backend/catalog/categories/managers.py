from django.db import models


from . import querysets


class BaseManager(models.Manager):
    pass


CategoryManager = BaseManager.from_queryset(querysets.CategoryQuerySet)