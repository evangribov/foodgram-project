# Generated by Django 3.1.6 on 2021-03-21 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким username уже существует.'}, max_length=50, unique=True, verbose_name='Логин'),
        ),
    ]
