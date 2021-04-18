# Generated by Django 3.2 on 2021-04-16 10:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название рубрики')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')], verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('nickname', models.CharField(help_text='Должен быть уникальным', max_length=30, unique=True, verbose_name='Никнейм')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('edited_time', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.rubric')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.user')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
