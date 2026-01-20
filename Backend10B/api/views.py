from django.shortcuts import render
from rest_framework import viewsets
from api.models import Group, User, Profile, Blitz, Match, Chat, Message
from api.serializers import GroupSerializer, UserSerializer, ProfileSerializer, BlitzSerializer, MatchSerializer, ChatSerializer, MessageSerializer

from rest_framework import generics

# Create your views here.

# Group API ViewSet
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# User API ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profile API ViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Blitz API ViewSet
class BlitzViewSet(viewsets.ModelViewSet):
    queryset = Blitz.objects.all()
    serializer_class = BlitzSerializer

# Match API ViewSet
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# Chat API ViewSet
class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

# Message API ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
