from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers import NoteSerializer
from ..filters import NoteFilter
from ..models import Note


class NoteViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 20
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NoteFilter

    def get_queryset(self):
        queryset = Note.objects.filter(diary__user=self.request.user)
        if self.action in ['retrieve', 'list']:
            queryset = Note.objects.all()
        return queryset

