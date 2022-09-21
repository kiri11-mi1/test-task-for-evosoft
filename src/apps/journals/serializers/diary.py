from rest_framework import serializers

from ..models import Diary
from ..constants import DiaryTypes, DiaryErrors
from ...users.serializers import UserSummarySerializer


class DiaryCreateSerializer(serializers.ModelSerializer):

    def validate(self, data: dict):
        expiration = data.get('expiration')
        kind = data.get('kind')

        if expiration and kind == DiaryTypes.PUBLIC:
            raise serializers.ValidationError(DiaryErrors.ONLY_PRIVATE)

        return data

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
