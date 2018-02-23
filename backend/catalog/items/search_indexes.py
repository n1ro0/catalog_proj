from django.utils import timezone
from haystack import indexes
from . import models


class ItemIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    price = indexes.FloatField(model_attr='price')
    description = indexes.CharField(model_attr='description')
    created_at = indexes.DateTimeField(model_attr='created_at')
    modified_at = indexes.DateTimeField(model_attr='modified_at')
    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.name, str(obj.price)
        ))

    def get_model(self):
        return models.Item

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            created_at__lte=timezone.now()
        )
