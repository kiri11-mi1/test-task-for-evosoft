from django_filters import rest_framework as filters, CharFilter, ChoiceFilter, DateFilter

from ..models import Diary
from ..constants import DiaryTypes


class DiaryFilter(filters.FilterSet):
    title = CharFilter('title')
    kind = ChoiceFilter(choices=DiaryTypes.CHOICES)
    expiration = DateFilter('expiration', lookup_expr='gte')
    username = CharFilter('user__username')
    login = CharFilter('user__login')

    class Meta:
        model = Diary
        fields = ('title', 'kind', 'expiration', 'login', 'username',)
