from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


from . import serializers
from . import models


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    queryset = models.BaseUser.objects.all()
    serializer_class = serializers.UserSerializer


class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
