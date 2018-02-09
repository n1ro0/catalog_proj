from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = [
    path(r'users/', UserList.as_view(), name='user-list'),
    path(r'users/<int:pk>/', UserDetail.as_view(), name='baseuser-detail'),
    path(r'groups/', GroupList.as_view(), name='group-list'),
    path(r'groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += [path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
