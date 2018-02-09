from rest_framework import serializers


from catalog.categories import models as categories_models
from . import models


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=categories_models.Category.objects.all()
    )

    class Meta:
        model = models.Item
        fields = (
            'url', 'id', 'name', 'price', 'categories', 'image'
        )
        read_only_fields = (
            'url', 'id', 'created_at', 'modified_at', 'image'
        )


class DetailItemSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, slug_field='name',
        queryset=categories_models.Category.objects.all()
    )

    class Meta:
        model = models.Item
        fields = (
            'id', 'name', 'price', 'categories',
            'description', 'image'
        )
        read_only_fields = (
            'id', 'created_at', 'modified_at', 'image'
        )
