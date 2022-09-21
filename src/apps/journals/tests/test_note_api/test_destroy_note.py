import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from apps.journals.models import Note


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


def test_delete_note_by_anon_user(api_client, note):
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client.delete(tmp_url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Note.objects.count() == 1


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_delete_note(api_client_with_user, note, diary):
    user = api_client_with_user.handler._force_user
    diary.user = user
    diary.save()

    note.diary = diary
    note.save()

    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.delete(tmp_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Note.objects.count() == 0


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_delete_foreign_note(api_client_with_user, note):
    """Удаление дневника, который не принадлжит пользователю"""
    tmp_url = reverse('api:journals:note-detail', args=(note.id,))
    response = api_client_with_user.delete(tmp_url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert Note.objects.count() == 1
