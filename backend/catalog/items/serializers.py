from rest_framework import serializers
from drf_haystack import serializers as haystack_serializers


from catalog.categories import models as categories_models
from catalog.categories import serializers as categories_serializers
from . import models
from . import search_indexes


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True, slug_field='name',
        read_only=True
    )
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = models.Item
        fields = (
            'url', 'id', 'name', 'price', 'categories', 'image', 'rating'
        )
        read_only_fields = (
            'url', 'id', 'created_at', 'modified_at', 'image', 'rating'
        )


class DetailItemSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

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


class RateSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.Rate
        fields = ('score', 'created_at', 'modified_at', 'username')
        read_only_fields = ('created_at', 'modified_at')


class ItemIndexSerializer(haystack_serializers.HaystackSerializer):

    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [search_indexes.ItemIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", 'id', "name", 'price', 'description', 'created_at', 'modified_at', 'autocomplete'
        ]
