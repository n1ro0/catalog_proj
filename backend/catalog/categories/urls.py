from rest_framework import routers


from . import viewsets


router = routers.DefaultRouter()
router.register('categories/search', viewsets.CategorySearchViewSet, base_name='categories-search')
router.register(r'categories', viewsets.CategoryModelViewSet, base_name='category')
urlpatterns = router.get_urls()
