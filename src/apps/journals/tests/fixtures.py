import pytest
from mixer.backend.django import mixer
from apps.journals.models import Diary


@pytest.fixture
def diary():
    return mixer.blend(Diary)


@pytest.fixture
def diaries():
    return mixer.cycle(5).blend(Diary)


