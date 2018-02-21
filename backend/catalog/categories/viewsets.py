from rest_framework import viewsets
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
# from cacheback.decorators import cacheback
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        # print(request.user)
        # print(request.META)
        return Response(cached.Categories().get(name), status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def items(self, request, pk=None):
        name = request.query_params.get('name', None)
        return Response(cached.CategoryItems().get(name, pk), status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def sub_categories(self, request, pk=None):
        categories = models.Category.objects.get(pk=pk).sub_categories.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
