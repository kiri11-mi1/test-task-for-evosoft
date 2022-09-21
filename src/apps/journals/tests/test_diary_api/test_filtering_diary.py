from random import choices

import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status


from ...serializers import DiarySerializer
from ...models import Diary


pytestmark = [pytest.mark.django_db]

AUTH_DATA = [
    {
        'email': mixer.faker.email(),
        'password': mixer.faker.password(),
        'username': mixer.faker.word().title()
    }
]


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_by_username(api_client_with_user, diaries):
    diary = choices(diaries)[0]
    filtering_diaries = Diary.objects.filter(user__username=diary.user.username)
    data = DiarySerializer(filtering_diaries, many=True).data

    expected = {
        'count': len(filtering_diaries),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?username={diary.user.username}'
    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_by_kind(api_client_with_user, diaries):
    diary = choices(diaries)[0]
    filtering_diaries = Diary.objects.filter(kind=diary.kind)
    data = DiarySerializer(filtering_diaries, many=True).data

    expected = {
        'count': len(filtering_diaries),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?kind={diary.kind}'
    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_with_wrong_kind(api_client_with_user):
    kind = mixer.faker.word().title()
    query_params = f'?kind={kind}'

    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_by_login(api_client_with_user, diaries):
    diary = choices(diaries)[0]
    filtering_diaries = Diary.objects.filter(user__login=diary.user.login)
    data = DiarySerializer(filtering_diaries, many=True).data

    expected = {
        'count': len(filtering_diaries),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?login={diary.user.login}'
    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_by_title(api_client_with_user, diaries):
    diary = choices(diaries)[0]
    filtering_diaries = Diary.objects.filter(title=diary.title)
    data = DiarySerializer(filtering_diaries, many=True).data

    expected = {
        'count': len(filtering_diaries),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?title={diary.title}'
    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected


@pytest.mark.parametrize('auth_data', AUTH_DATA)
def test_filter_diary_by_expiration(api_client_with_user, diaries_with_expiration):
    diary = choices(diaries_with_expiration)[0]
    filtering_diaries = Diary.objects.filter(expiration=diary.expiration)
    data = DiarySerializer(filtering_diaries, many=True).data

    expected = {
        'count': len(filtering_diaries),
        'next': None,
        'previous': None,
        'results': data
    }

    query_params = f'?expiration={diary.expiration}'
    tmp_url = reverse('api:journals:diary-list') + query_params
    response = api_client_with_user.get(tmp_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected
