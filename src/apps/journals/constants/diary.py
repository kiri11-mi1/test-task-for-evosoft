from typing import Final


class DiaryTypes:
    PUBLIC: Final[str] = 'public'
    PRIVATE: Final[str] = 'private'

    CHOICES: Final[tuple[tuple[str, str], ...]] = (
        (PUBLIC, 'Публичный'),
        (PRIVATE, 'Приватный'),
    )

    CHOICES_DICT: Final[dict[str, str]] = dict(CHOICES)
