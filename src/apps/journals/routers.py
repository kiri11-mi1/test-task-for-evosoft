from rest_framework.routers import DefaultRouter

from .viewsets import DiaryViewSet

journals_router = DefaultRouter()

journals_router.register(
    prefix='diary',
    viewset=DiaryViewSet,
    basename='diary',
)
# journals_router.register(
#     prefix='categories',
#     viewset=TransactionCategoryViewSet,
#     basename='categories',
# )
