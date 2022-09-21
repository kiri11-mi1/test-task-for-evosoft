from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, pagination

from ..models import Diary
from ..serializers import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 20
    permission_classes = (IsAuthenticated,)
    serializer_class = DiarySerializer

    def get_queryset(self):
        queryset = Diary.objects.filter(user=self.request.user)
        if self.action in ['retrieve', 'list']:
            queryset = Diary.objects.all()
        return queryset
