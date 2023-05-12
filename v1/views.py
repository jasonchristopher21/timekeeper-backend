from django.shortcuts import render

from rest_framework import viewsets

from .serializers import DeckSerializer, SlideSerializer
from .models import Deck, Slide

# Create your views here.
class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all().order_by('name')
    serializer_class = DeckSerializer

class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all().order_by('slide_number')
    serializer_class = SlideSerializer