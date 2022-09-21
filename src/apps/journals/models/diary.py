from django.db import models
from django.contrib.auth import get_user_model

from ..constants import DiaryTypes


class Diary(models.Model):
    title = models.CharField('Название', max_length=128)
    kind = models.CharField(
        max_length=50,
        choices=DiaryTypes.CHOICES,
        verbose_name='Тип дневника',
    )
    expiration = models.DateField(
        'Срок действия',
        help_text='Дата, после которой можно удалить дневник',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='diaries',
    )

    def __str__(self):
        return f'{self.title}({self.kind})'

    class Meta:
        verbose_name = 'Дневник'
        verbose_name_plural = 'Дневники'
