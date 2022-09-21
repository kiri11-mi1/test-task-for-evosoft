from rest_framework import serializers

from ..models import Note


class NoteSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.diary = validated_data.get('diary', instance.diary)
        instance.save()
        return instance

    class Meta:
        model = Note
        fields = ('id', 'text', 'diary',)
