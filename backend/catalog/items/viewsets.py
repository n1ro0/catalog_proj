from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import models as dj_models


from rest_framework import (
    viewsets,
    status,
    parsers,
    decorators
)
from rest_framework.response import Response


from . import serializers
from . import models
from . import cached


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.with_rating()
    serializer_class = serializers.DetailItemSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        return Response(cached.ItemDetail().get(pk), status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        sort = request.query_params.get('sort', None)
        if sort:
            if sort == 'desc':
                items = self.get_queryset().order_by('-price')
            elif sort == 'asc':
                items = self.get_queryset().order_by('price')
            else:
                items = self.get_queryset()
        else:
            items = self.get_queryset()
        serializer = serializers.ListItemSerializer(items, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def comments(self, request, pk, *args, **kwargs):
        comments = self.get_queryset().get(pk=pk).comments.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @decorators.detail_route(methods=['get'])
    def rates(self, request, pk, *args, **kwargs):
        rates = self.get_queryset().get(pk=pk).rates.select_related('user')
        serializer = serializers.RateSerializer(rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @decorators.parser_classes((parsers.FormParser, parsers.MultiPartParser))
    # def create(self, request, format=None):
    #     print(request.data)
    #     serializer = serializers.ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

