from django_filters import rest_framework as filters, CharFilter, ChoiceFilter, DateFilter

from ..models import Note


class NoteFilter(filters.FilterSet):
    text = CharFilter('text')
    diary = CharFilter('diary__title')

    class Meta:
        model = Note
        fields = ('text', 'diary',)
