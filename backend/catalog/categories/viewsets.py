from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response


from . import serializers
from . import models
from catalog.items import (
    serializers as items_serializers,
    models as items_models
)


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing trend instances.
    """
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    @decorators.detail_route(methods=['get'])
    def items(self, request, pk=None):
        items = models.Category.objects.get(pk=pk).items.all()
        serializer = items_serializers.ListItemSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)

    @decorators.detail_route(methods=['get'])
    def sub_categories(self, request, pk=None):
        categories = models.Category.objects.get(pk=pk).sub_categories.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)
