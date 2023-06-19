from rest_framework import serializers
from .models import Post, Directory


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = "__all__"
