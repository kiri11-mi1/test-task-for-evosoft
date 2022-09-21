from random import choices

import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status


from ...serializers import NoteSerializer
from ...models import Note


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_note_by_text(api_client_with_user, notes):
    note = choices(notes)[0]
    filtering_notes = Note.objects.filter(text=note.text)
    data = NoteSerializer(filtering_notes, many=True).data

    expected = {
        'count': len(filtering_notes),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?text={note.text}'
    tmp_url = reverse('api:journals:note-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_note_by_diary_title(api_client_with_user, notes):
    note = choices(notes)[0]
    filtering_notes = Note.objects.filter(diary__title=note.diary.title)
    data = NoteSerializer(filtering_notes, many=True).data

    expected = {
        'count': len(filtering_notes),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?diary={note.diary.title}'
    tmp_url = reverse('api:journals:note-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected
