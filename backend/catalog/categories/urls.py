from rest_framework import routers


from . import viewsets


router = routers.DefaultRouter()
router.register(r'categories', viewsets.CategoryModelViewSet, base_name='category')
urlpatterns = router.get_urls()
