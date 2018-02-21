from django.db import models as dj_models


from cacheback.base import Job


from . import models
from . import serializers


class ItemDetail(Job):
    lifetime = 60 * 5

    def fetch(self, pk, *args, **kwargs):
        item = models.Item.objects.with_rating().get(pk=pk)
        serializer = serializers.DetailItemSerializer(item)
        return serializer.data


