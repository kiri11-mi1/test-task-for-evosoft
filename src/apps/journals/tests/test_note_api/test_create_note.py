from random import randint as rd

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


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_note_with_not_exist_diary(api_client_with_user):
    payload = {
        'text': mixer.faker.word(),
        'diary': rd(1, 19),
    }
    tmp_url = reverse('api:journals:note-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Note.objects.count() == 0


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_note_without_diary(api_client_with_user):
    payload = {
        'text': mixer.faker.word()
    }
    tmp_url = reverse('api:journals:note-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Note.objects.count() == 0


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_note_without_text(api_client_with_user, diary):
    payload = {
        'diary': diary.id
    }
    tmp_url = reverse('api:journals:note-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Note.objects.count() == 0


def test_create_note_by_anon_user(api_client, diary):
    payload = {
        'text': mixer.faker.word(),
        'diary': diary.id,
    }
    tmp_url = reverse('api:journals:note-list')
    response = api_client.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Note.objects.count() == 0


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_note(api_client_with_user, diary):
    payload = {
        'text': mixer.faker.word(),
        'diary': diary.id,
    }
    tmp_url = reverse('api:journals:note-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    json = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert Note.objects.count() == 1
