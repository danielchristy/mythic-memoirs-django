from django.shortcuts import render
from .models import Session
from rest_framework import generics
from .serializers import SessionSerializer

# Create your views here.

#list of all sessions
class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

#individual session data
class SessionDetail(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer