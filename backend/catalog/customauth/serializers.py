from django.contrib.auth.models import Group, Permission
from rest_framework import serializers


from . import models


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = models.BaseUser.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = models.BaseUser
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.SlugRelatedField(
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
