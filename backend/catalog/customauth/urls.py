from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt


from rest_framework.urlpatterns import format_suffix_patterns


from .views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = [
    url(r'users/', UserList.as_view(), name='user-list'),
    url(r'users/(?P<pk>\d+)/', UserDetail.as_view(), name='baseuser-detail'),
    url(r'groups/', GroupList.as_view(), name='group-list'),
    url(r'groups/(?P<pk>\d+)/', GroupDetail.as_view(), name='group-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += [url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
