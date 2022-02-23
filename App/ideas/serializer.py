from .models import Idea, Vote
from rest_framework import serializers


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'app_url', 'status']


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Mata:
        model = Vote
        fields = ['idea', 'reason']
