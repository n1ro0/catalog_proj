import time


from django.utils import timezone
from django.db import models as dj_models


from cacheback.decorators import cacheback
from cacheback.base import Job


from . import serializers
from . import models
from catalog.items import serializers as items_serializers


class Categories(Job):
    def fetch(self):
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return serializer.data

    def expiry(self):
        now = time.time()
        return now + 60 * 5


class CategoryItems(Job):
    lifetime = 60 * 5

    def fetch(self, pk):
        items = models.Category.objects.get(pk=pk).items.with_rating()
        serializer = items_serializers.DetailItemSerializer(items, many=True)
        return serializer.data



# @cacheback(lifetime=60, fetch_on_miss=False)
# def categories_by_name(name):
#     if name:
#         categories = models.Category.objects.filter(name__icontains=name)
#     else:
#         categories = models.Category.objects.all()
#     serializer = serializers.CategorySerializer(categories, many=True)
#     return serializer.data
