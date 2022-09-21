import pytest
from mixer.backend.django import mixer
from apps.journals.models import Diary, Note

from ..constants import DiaryTypes


@pytest.fixture
def diary():
    return mixer.blend(Diary)


@pytest.fixture
def diaries():
    return mixer.cycle(5).blend(Diary)


@pytest.fixture
def diaries_with_expiration():
    return mixer.cycle(5).blend(
        Diary,
        expiration=mixer.faker.date(),
        kind=DiaryTypes.PRIVATE
    )


@pytest.fixture
def note():
    return mixer.blend(Note, diary=mixer.blend(Diary))


@pytest.fixture
def notes():
    return mixer.cycle(5).blend(Note, diary=mixer.blend(Diary))
