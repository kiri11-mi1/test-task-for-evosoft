import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status

from apps.journals.models import Diary


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


def test_delete_diary_by_anon_user(api_client, diary):
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client.delete(tmp_url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Diary.objects.count() == 1


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_delete_diary(api_client_with_user, diary):
    user = api_client_with_user.handler._force_user
    diary.user = user
    diary.save()

    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.delete(tmp_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Diary.objects.count() == 0


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_delete_foreign_diary(api_client_with_user, diary):
    """Удаление дневника, который не принадлжит пользователю"""
    tmp_url = reverse('api:journals:diary-detail', args=(diary.id,))
    response = api_client_with_user.delete(tmp_url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert Diary.objects.count() == 1
