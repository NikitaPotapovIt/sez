from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']
        read_only_fields = ['author']

    def validate(self, attrs):
        attrs['author'] = self.context['request'].user
        return attrs
