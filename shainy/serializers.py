from rest_framework import serializers
from .models import PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('event', 'event_date', 'description')

class ShowPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('event', 'event_date', 'description', 'user', 'date_pub')
