from rest_framework import routers


from . import viewsets
from . import views


router = routers.DefaultRouter()
router.register(r"items/search", views.ItemsSearchView, base_name="items-search")
router.register(r'items', viewset=viewsets.ItemModelViewSet, base_name='item')
urlpatterns = router.get_urls()
