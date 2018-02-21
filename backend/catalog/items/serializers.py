from rest_framework import serializers


from catalog.categories import models as categories_models
from catalog.categories import serializers as categories_serializers
from . import models


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, slug_field='name',
        read_only=True
    )
    rating = serializers.FloatField()

    class Meta:
        model = models.Item
        fields = (
            'url', 'id', 'name', 'price', 'categories', 'image', 'rating'
        )
        read_only_fields = (
            'url', 'id', 'created_at', 'modified_at', 'image', 'rating'
        )


class DetailItemSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = models.Item
        fields = (
            'id', 'name', 'price', 'categories',
            'description', 'image', 'rating'
        )
        read_only_fields = (
            'id', 'created_at', 'modified_at', 'rating'
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = ('text', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
