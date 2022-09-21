import pytest
from mixer.backend.django import mixer
from apps.journals.models import Diary, Note


@pytest.fixture
def diary():
    return mixer.blend(Diary)


@pytest.fixture
def diaries():
    return mixer.cycle(5).blend(Diary)


@pytest.fixture
def note():
    return mixer.blend(Note)


@pytest.fixture
def notes():
    return mixer.cycle(5).blend(Note)
