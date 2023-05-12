from rest_framework import serializers

from .models import Deck, Slide

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ('name', 'description', 'date', 'last_modified')

class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slide
        fields = ('deck_id', 'slide_number', 'title', 'content', 'duration')