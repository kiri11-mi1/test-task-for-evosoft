from random import randint as rd

import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from apps.journals.serializers import NoteSerializer


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


def test_update_note_by_anon_user(api_client, note):
    payload = {
        'text': mixer.faker.word().title(),
        'diary': note.diary.id,
    }
    tmp_url = reverse('api:journals:note-detail', args=(note.diary.id,))
    response = api_client.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_foreign_note(api_client_with_user, note):
    payload = {
        'text': mixer.faker.word().title(),
        'diary': note.diary.id,
    }
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_note(api_client_with_user, note, diary):
    note.diary.user = api_client_with_user.handler._force_user
    note.diary.save()
    note.save()

    payload = {
        'text': mixer.faker.word().title(),
        'diary': note.diary.id,
    }

    expected = NoteSerializer(note).data
    expected['text'] = payload['text']
    expected['diary'] = payload['diary']

    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_note_with_not_exist_diary(api_client_with_user, note):
    note.diary.user = api_client_with_user.handler._force_user
    note.diary.save()
    note.save()

    payload = {
        'text': mixer.faker.word(),
        'diary': rd(1, 19),
    }
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_note_without_diary(api_client_with_user, note):
    note.diary.user = api_client_with_user.handler._force_user
    note.diary.save()
    note.save()

    payload = {
        'text': mixer.faker.word(),
    }
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_note_without_text(api_client_with_user, note):
    note.diary.user = api_client_with_user.handler._force_user
    note.diary.save()
    note.save()

    payload = {
        'diary': note.diary.id,
    }
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
