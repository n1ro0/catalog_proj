from rest_framework import viewsets


from . import serializers
from . import models


class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing trend instances.
    """
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
