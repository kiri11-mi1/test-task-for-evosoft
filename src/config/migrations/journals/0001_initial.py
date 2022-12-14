# Generated by Django 3.2.2 on 2022-09-21 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('kind', models.CharField(choices=[('public', 'Публичный'), ('private', 'Приватный')], max_length=50, verbose_name='Тип дневника')),
                ('expiration', models.DateField(blank=True, help_text='Дата, после которой можно удалить дневник', null=True, verbose_name='Срок действия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Дневник',
                'verbose_name_plural': 'Дневники',
            },
        ),
    ]
