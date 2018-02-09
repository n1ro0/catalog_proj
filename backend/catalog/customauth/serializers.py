from django.contrib.auth.models import Group, Permission
from rest_framework import serializers


from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BaseUser
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.SlugRelatedField(
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
