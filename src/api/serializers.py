from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user','title', 'content', 'created_datetime']
        read_only_fields = ['id', 'user', 'created_datetime']