from rest_framework import (
    viewsets,
    status,
    parsers,
    decorators
)

from rest_framework.response import Response


from . import serializers
from . import models


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.DetailItemSerializer

    def list(self, request, *args, **kwargs):
        items = self.get_queryset()
        serializer = serializers.ListItemSerializer(items, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



    # @decorators.parser_classes((parsers.FormParser, parsers.MultiPartParser))
    # def create(self, request, format=None):
    #     print(request.data)
    #     serializer = serializers.ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

