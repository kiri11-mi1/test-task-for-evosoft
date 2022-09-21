import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status


from apps.journals.constants import DiaryTypes
from apps.journals.models import Diary


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_private_diary_with_expiration(api_client_with_user):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PRIVATE,
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Diary.objects.count() == 1


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_private_diary_not_expiration(api_client_with_user):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PRIVATE
    }
    tmp_url = reverse('api:journals:diary-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Diary.objects.count() == 1


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_public_diary_with_expiration(api_client_with_user):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PUBLIC,
        'expiration': mixer.faker.date()
    }
    tmp_url = reverse('api:journals:diary-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_create_public_diary_not_expiration(api_client_with_user):
    payload = {
        'title': mixer.faker.word().title(),
        'kind': DiaryTypes.PUBLIC
    }
    tmp_url = reverse('api:journals:diary-list')
    response = api_client_with_user.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Diary.objects.count() == 1
