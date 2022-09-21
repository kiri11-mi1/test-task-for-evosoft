import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from django.contrib.auth import get_user_model

from ..serializers import UserSummarySerializer
from ..models import User

pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_user_me(api_client_with_user):
    user = api_client_with_user.handler._force_user
    expected = UserSummarySerializer(user).data
    tmp_url = reverse('api:users:me')

    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


def test_user_login(api_client):
    password = mixer.faker.password()
    user = mixer.blend(get_user_model())
    user.set_password(password)
    user.save()

    payload = {
        'email': user.email,
        'password': password
    }

    tmp_url = reverse('api:auth:token')
    response = api_client.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_200_OK


def test_user_register(api_client):
    email = mixer.faker.email(),
    password = mixer.faker.password(),
    username = mixer.faker.word().title()

    payload = {
        'email': email,
        'username': username,
        'password': password
    }

    tmp_url = reverse('api:auth:register')
    response = api_client.post(tmp_url, data=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
