from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from api.models import Group, User, Profile, Blitz, Match, Chat, Message
from api.serializers import GroupSerializer, UserSerializer, ProfileSerializer, BlitzSerializer, MatchSerializer, ChatSerializer, MessageSerializer

from rest_framework import generics

# Create your views here.

# Group API ViewSet
@extend_schema(tags=['Groups'])
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# User API ViewSet
@extend_schema(tags=['Users'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profile API ViewSet
@extend_schema(tags=['Profiles'])
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Blitz API ViewSet
@extend_schema(tags=['Blitzes'])
class BlitzViewSet(viewsets.ModelViewSet):
    queryset = Blitz.objects.all()
    serializer_class = BlitzSerializer

# Match API ViewSet
@extend_schema(tags=['Matches'])
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# Chat API ViewSet
@extend_schema(tags=['Chats'])
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

# Message API ViewSet
@extend_schema(tags=['Messages'])
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
