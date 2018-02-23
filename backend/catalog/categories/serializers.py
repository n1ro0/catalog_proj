from rest_framework import serializers
from drf_haystack import serializers as haystack_serializers


from . import models
from . import search_indexes


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    sub_categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Category
        fields = (
            'id', 'name', 'parent_category', 'sub_categories'
        )
        read_only_fields = ('created_at', 'modified_at', 'sub_categories')


class CategorySmallSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = models.Category
        fields = (
            'id', 'name'
        )
        read_only_fields = ('created_at', 'modified_at')


class CategoryIndexSerializer(haystack_serializers.HaystackSerializer):

    class Meta:
        index_classes = (search_indexes.CategoryIndex, )
        fields = ('text', "my_id", 'name', 'created_at', 'modified_at', 'autocomplete')
