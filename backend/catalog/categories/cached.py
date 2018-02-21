import time


from django.utils import timezone
from django.db import models as dj_models


from cacheback.decorators import cacheback
from cacheback.base import Job


from . import serializers
from . import models
from catalog.items import serializers as items_serializers


class Categories(Job):
    def fetch(self, name):
        if name == '' or name is None:
            categories = models.Category.objects.all()
        else:
            categories = models.Category.objects.filter(name__icontains=name)
        serializer = serializers.CategorySerializer(categories, many=True)
        return serializer.data

    def expiry(self, name):
        now = time.time()
        return now + 60 * 5


class CategoryItems(Job):
    lifetime = 60

    def fetch(self, name, pk):
        if name == '' or name is None:
            items = models.Category.objects.get(pk=pk).items.annotate(rating=dj_models.Avg('rates__score'))
        else:
            items = models.Category.objects.get(pk=pk).items.filter(name__icontains=name)\
                .annotate(rating=dj_models.Avg('rates__score'))
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
