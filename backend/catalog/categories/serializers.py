from rest_framework import serializers


from . import models


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
