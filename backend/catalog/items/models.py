from django.db import models


from . import managers
from catalog.core import models as core_models
from catalog.customauth import models as auth_models
from catalog.categories import models as categories_models


def upload_to(instance, filename):
    return 'items/{}/{}'.format(instance.id, 'photo.png')


class Item(core_models.TimeStamped):
    name = models.CharField(max_length=300, blank=True)
    price = models.FloatField(null=True, blank=True)
    categories = models.ManyToManyField(categories_models.Category, related_name='items')
    description = models.TextField(blank=True)
    image = models.ImageField(default='items/default.png', upload_to=upload_to)
    objects = managers.ItemManager()

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)


class Rate(core_models.TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey(auth_models.BaseUser, on_delete=models.CASCADE, related_name='rates')
    score = models.IntegerField()


class Comment(core_models.TimeStamped):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(auth_models.BaseUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
