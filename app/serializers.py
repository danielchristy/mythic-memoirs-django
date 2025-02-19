from rest_framework import serializers
from .models import Session, Character, Location

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
    
class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'