from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
from drf_haystack.viewsets import HaystackViewSet
# from cacheback.decorators import cacheback
from rest_framework.permissions import IsAdminUser


from . import serializers
from . import models
from catalog.items import (
    serializers as items_serializers,
    models as items_models
)
from . import cached
from . import helpers


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing trend instances.
    """
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name is None or name == '':
            categories = cached.Categories().get()
        else:
            categories = models.Category.objects.filter(name__icontains=name)
            serializer = serializers.CategorySerializer(categories, many=True)
            categories = serializer.data
        return Response(categories, status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def items(self, request, pk=None):
        name = request.query_params.get('name', None)
        if name is None or name == '':
            items = cached.CategoryItems().get(pk)
        else:
            items = models.Category.objects.get(pk=pk).items.filter(name__icontains=name) \
                .with_rating()
            serializer = items_serializers.DetailItemSerializer(items, many=True)
            items = serializer.data
        return Response(items, status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def sub_categories(self, request, pk=None):
        categories = models.Category.objects.get(pk=pk).sub_categories.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategorySearchViewSet(HaystackViewSet):

    index_models = (models.Category,)
    serializer_class = serializers.CategoryIndexSerializer
