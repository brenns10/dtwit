from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Tweet
from . import serializers
from .permissions import IsOwnerOrReadOnly


class TweetList(generics.ListCreateAPIView):
    """
    List all tweets, or create a new one.
    """

    queryset = Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TweetDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a tweet.
    """

    queryset = Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    """
    List all users.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a single user.
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
