from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'content', 'debut']
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'singer', 'release', 'content']
        read_only_fields = ['singer']