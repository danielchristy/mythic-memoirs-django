from django.shortcuts import render
from .models import Session, Character, Location
from rest_framework import generics
from .serializers import *

#Session return all & return specific
class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetail(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

#Character return all & return specific
class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer

class CharacterDetail(generics.RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharactersSerializer

#Location return all & return specific
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer