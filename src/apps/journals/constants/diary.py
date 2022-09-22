from typing import Final

TIME_DELETING_OLD_DIARY = 10.0*60.0


class DiaryTypes:
    PUBLIC: Final[str] = 'public'
    PRIVATE: Final[str] = 'private'

    CHOICES: Final[tuple[tuple[str, str], ...]] = (
        (PUBLIC, 'Публичный'),
        (PRIVATE, 'Приватный'),
    )

    CHOICES_DICT: Final[dict[str, str]] = dict(CHOICES)
