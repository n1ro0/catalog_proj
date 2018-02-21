from django.contrib import admin


from . import models


admin.site.register((models.Item, models.Rate, models.Comment))
