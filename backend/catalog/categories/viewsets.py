from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status


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

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name:
            categories = self.get_queryset().filter(name__icontains=name)
        else:
            categories = self.get_queryset()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def items(self, request, pk=None):
        name = request.query_params.get('name', None)
        if name:
            items = models.Category.objects.get(pk=pk).items.filter(name__icontains=name)
        else:
            items = models.Category.objects.get(pk=pk).items.all()
        serializer = items_serializers.ListItemSerializer(items, many=True, context={'request': request})
        return Response(serializer.data)

    @decorators.detail_route(methods=['get'])
    def sub_categories(self, request, pk=None):
        categories = models.Category.objects.get(pk=pk).sub_categories.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)
