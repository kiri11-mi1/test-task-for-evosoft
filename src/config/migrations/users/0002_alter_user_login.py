# Generated by Django 3.2.2 on 2022-09-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Login'),
        ),
    ]
