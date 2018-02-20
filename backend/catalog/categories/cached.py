import time


from django.utils import timezone


from cacheback.decorators import cacheback
from cacheback.base import Job


from . import serializers
from . import models
from catalog.items import serializers as items_serializers


class Categories(Job):
    def fetch(self, name):
        name = name.replace('categories', '')
        if name == '':
            categories = models.Category.objects.all()
        else:
            categories = models.Category.objects.filter(name__icontains=name)
        serializer = serializers.CategorySerializer(categories, many=True)
        return serializer.data

    def expiry(self, name):
        now = time.time()
        return now + 60 * 5



# @cacheback(lifetime=60, fetch_on_miss=False)
# def categories_by_name(name):
#     if name:
#         categories = models.Category.objects.filter(name__icontains=name)
#     else:
#         categories = models.Category.objects.all()
#     serializer = serializers.CategorySerializer(categories, many=True)
#     return serializer.data
