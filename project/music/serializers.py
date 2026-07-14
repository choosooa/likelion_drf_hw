from rest_framework import serializers
from .models import *


class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    content = serializers.CharField()
    debut = serializers.CharField()
    
    songs = serializers.SerializerMethodField(read_only=True)
    tags =  serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(use_url=True, required=False)
    
    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data

    def get_tags(self, instance):
        tags = instance.tags.all()
        return [tag.name for tag in tags]
    
    class Meta:
        model = Singer
        fields = ['id', 'content', 'debut', 'tags', 'image', 'songs']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'singer', 'release', 'content']
        read_only_fields = ['singer']
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'