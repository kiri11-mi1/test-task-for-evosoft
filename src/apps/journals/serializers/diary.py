from rest_framework import serializers

from ..models import Diary
from ..constants import DiaryTypes, DiaryErrors
from ...users.serializers import UserSummarySerializer


class DiaryCreateSerializer(serializers.ModelSerializer):

    def validate(self, data: dict):
        expiration = data.get('expiration')
        kind = data.get('kind')

        if not expiration and self.instance:
            expiration = self.instance.expiration
    
        if expiration and kind == DiaryTypes.PUBLIC:
            raise serializers.ValidationError(DiaryErrors.ONLY_PRIVATE)

        return data

    def update(self, instance, validated_data):
        instance.kind = validated_data.get('kind', instance.kind)
        instance.expiration = validated_data.get('expiration', instance.expiration)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    def create(self, validated_data: dict):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Diary
        fields = ('id', 'title', 'kind', 'expiration',)


class DiaryReadSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer()

    class Meta:
        model = Diary
        fields = ('id', 'title', 'kind', 'expiration', 'user',)
