from .models import UserPost, Album, Files
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = UserPost
        #fields = ['title', 'body']
        fields = ['pk', 'author_name', 'title', 'body']
        #read_only_fields = ('title',)

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')

class FileSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    files = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'files', 'desc')
        