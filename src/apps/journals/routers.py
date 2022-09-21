from rest_framework.routers import DefaultRouter

from .viewsets import DiaryViewSet, NoteViewSet

journals_router = DefaultRouter()

journals_router.register(
    prefix='diary',
    viewset=DiaryViewSet,
    basename='diary',
)
journals_router.register(
    prefix='note',
    viewset=NoteViewSet,
    basename='note',
)
