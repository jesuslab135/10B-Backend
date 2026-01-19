from django.shortcuts import render
from api.models import Group, User, Profile, Blitz, Match, Chat, Message
from api.serializers import GroupSerializer, UserSerializer, ProfileSerializer, BlitzSerializer, MatchSerializer, ChatSerializer, MessageSerializer

from rest_framework import generics

# Create your views here.

# Group API Views
class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# User API Views
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profile API Views
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = Profile.objects.all()

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Blitz API Views
class BlitzList(generics.ListCreateAPIView):
    queryset = Blitz.objects.all()
    serializer_class = Blitz.objects.all()

class BlitzDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blitz.objects.all()
    serializer_class = BlitzSerializer

# Match API Views
class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = Match.objects.all()

class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# Chat API Views
class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = Chat.objects.all()

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

# Message API Views
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = Message.objects.all()

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer