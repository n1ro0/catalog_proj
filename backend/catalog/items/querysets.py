from django.db import models


class ItemQuerySet(models.QuerySet):

    def with_rating(self):
        return self.annotate(rating=models.Avg('rates__score'))
