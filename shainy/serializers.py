from rest_framework import serializers
from .models import PostModel, ResponseModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('event', 'event_date', 'description')

class ShowPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('event', 'event_date', 'description', 'user', 'date_pub', 'id')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = ('post', 'user1', 'post_author', 'id')
