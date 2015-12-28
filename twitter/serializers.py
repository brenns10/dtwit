"""
Serializers for Twitter clone.
"""

from django.contrib.auth.models import User
from rest_framework import serializers as s

from .models import Tweet


class TweetSerializer(s.HyperlinkedModelSerializer):

    owner = s.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tweet
        fields = ('id', 'owner', 'created', 'text')


class UserSerializer(s.HyperlinkedModelSerializer):

    tweets = s.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = s.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'tweets', 'likes')
