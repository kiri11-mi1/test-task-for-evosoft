import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from apps.journals.serializers import DiarySerializer
from apps.journals.constants import DiaryTypes


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


def test_update_diary_by_anon_user(api_client, diary):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PRIVATE,
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_foreign_diary(api_client_with_user, diary):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PRIVATE,
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_diary(api_client_with_user, diary):
    user = api_client_with_user.handler._force_user
    diary.user = user
    diary.save()

    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PRIVATE,
        'expiration': mixer.faker.date()
    }

    expected = DiarySerializer(diary).data
    expected['title'] = payload['title']
    expected['kind'] = payload['kind']
    expected['expiration'] = payload['expiration']

    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_diary_with_wrong_kind(api_client_with_user, diary):
    user = api_client_with_user.handler._force_user
    diary.user = user
    diary.save()

    payload = {
        'title': mixer.faker.word().title(),
        'kind': mixer.faker.word().title(),
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_update_to_public_diary_with_expiration(api_client_with_user, diary):
    user = api_client_with_user.handler._force_user
    diary.user = user
    diary.kind = DiaryTypes.PRIVATE
    diary.save()

    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PUBLIC,
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.put(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
