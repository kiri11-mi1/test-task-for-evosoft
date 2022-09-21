from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, pagination

from ..models import Diary
from ..serializers import DiaryReadSerializer, DiaryCreateSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 20
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
