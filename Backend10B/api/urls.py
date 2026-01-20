from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r"groups", views.GroupViewSet, basename="group")
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"profiles", views.ProfileViewSet, basename="profile")
router.register(r"blitzes", views.BlitzViewSet, basename="blitz")
router.register(r"matches", views.MatchViewSet, basename="match")
router.register(r"chats", views.ChatViewSet, basename="chat")
router.register(r"messages", views.MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
]