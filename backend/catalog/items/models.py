from django.db import models


from . import managers
from catalog.core import models as core_models
from catalog.categories import models as categories_models


class Item(core_models.TimeStamped):
    name = models.CharField(max_length=300, blank=True)
    price = models.FloatField(null=True, blank=True)
    categories = models.ManyToManyField(categories_models.Category, related_name='items')
    description = models.TextField(blank=True)
    image = models.ImageField(default='items/photos/default.png', upload_to='items/photos')
    objects = managers.ItemManager()

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)
