from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from ggworks.ggworks_api.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'is_superuser', 'username')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'id', 'name')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = UserProfile
    fields = ('id', 'user_id', 'full_name', 'nick_name', 'email', 'photo', 'photo_small')


class TokenInfoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Token
    fields = ('url', 'key', 'created', 'user_id')
