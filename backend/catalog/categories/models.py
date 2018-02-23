from django.db import models


from . import managers
from catalog.core import models as core_models


class Category(core_models.TimeStamped):
    name = models.CharField(max_length=300)
    parent_category = models.ForeignKey(
        'self', related_name='sub_categories', on_delete=models.SET_NULL,
        null=True, blank=True
    )
    objects = managers.CategoryManager()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)
