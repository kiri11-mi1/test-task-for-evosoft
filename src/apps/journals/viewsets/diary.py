from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Diary
from ..serializers import DiaryReadSerializer, DiaryCreateSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Diary.objects.filter(user=self.request.user)
        if self.action in ['retrieve', 'list']:
            queryset = Diary.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return DiaryReadSerializer
        return DiaryCreateSerializer
