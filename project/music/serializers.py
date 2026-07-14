from rest_framework import serializers
from .models import *


class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data

    class Meta:
        model = Singer
        fields = ['id', 'content', 'debut', 'songs']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'singer', 'release', 'content']
        read_only_fields = ['singer']