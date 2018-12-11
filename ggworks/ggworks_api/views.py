#from django.shortcuts import render
from django.contrib.auth.models import User, Group
# from django.http import Http404
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from ggworks.ggworks_api.serializers import *
from ggworks.ggworks_api.models import UserProfile

# # import the logging library
# import logging

# # Get an instance of a logger
# logger = logging.getLogger(__name__)

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer

class TokenInfoViewSet(viewsets.ModelViewSet):
  queryset = Token.objects.all()
  serializer_class = TokenInfoSerializer


class CustomObtainAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    response = super(CustomObtainAuthToken, self).post(
        request, *args, **kwargs)
    token = Token.objects.get(key=response.data['token'])
    user = UserSerializer(User.objects.get(pk=token.user_id), context={'request': request}).data
    userProfile = UserProfileSerializer(UserProfile.objects.get(pk=token.user_id), context={'request': request}).data
    return Response({'token': token.key, 'userInfo': user, 'userProfile': userProfile})


class Logout(APIView):
  queryset = User.objects.all()

  def post(self, request, format=None):
    # simply delete the token to force a login
    request.user.auth_token.delete()
    content = {'Success': 'Token deleted'}
    return Response(content, status=status.HTTP_200_OK)
