from django.db import models


class Note(models.Model):
    text = models.TextField(verbose_name='Текст')
    diary = models.ForeignKey(
        to='journals.Diary',
        on_delete=models.CASCADE,
        verbose_name='Дневник',
        related_name='notes',
    )

    def __str__(self):
        return f'{self.text[:10]}... from {self.diary}'

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
