from rest_framework import serializers

from .models import Deck, Slide

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'name', 'description', 'date', 'last_modified')

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slide
        fields = ('id','deck_id', 'slide_number', 'title', 'content', 'duration')