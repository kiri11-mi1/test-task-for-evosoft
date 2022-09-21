import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status


from ...serializers import DiarySerializer


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


def test_get_diary_by_anon_user(api_client):
    tmp_url = reverse('api:journals:diary-list')
    response = api_client.get(tmp_url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_get_all_diary(api_client_with_user, diaries):
    data = DiarySerializer(diaries, many=True).data
    expected = {
        'count': len(diaries),
        'next': None,
        'previous': None,
        'results': data
    }
    tmp_url = reverse('api:journals:diary-list')
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_get_one_diary(api_client_with_user, diary):
    expected = DiarySerializer(diary).data
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_get_one_diary_by_anon_user(api_client, diary):
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client.get(tmp_url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
