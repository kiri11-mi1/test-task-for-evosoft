from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Diary
from ..serializers import DiarySerializer
from ..filters import DiaryFilter


class DiaryViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 20
    permission_classes = (IsAuthenticated,)
    serializer_class = DiarySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DiaryFilter

    def get_queryset(self):
        queryset = Diary.objects.filter(user=self.request.user)
        if self.action in ['retrieve', 'list']:
            queryset = Diary.objects.all()
        return queryset
