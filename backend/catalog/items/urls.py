from rest_framework import routers


from . import viewsets


router = routers.DefaultRouter()
router.register(r'items', viewset=viewsets.ItemModelViewSet, base_name='item')
urlpatterns = router.get_urls()
