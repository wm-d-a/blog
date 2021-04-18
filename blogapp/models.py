from django.db import models
from django.core import validators
from .buf import countries


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона',
                             null=True, blank=True,
                             validators=[validators.RegexValidator(
                                 regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                 message='Неправильно введен номер телефона')])  # DON'T WORK!!!!!
    country = models.CharField(max_length=30, choices=countries,
                               default='2')
    # models.CharField(max_length=30, verbose_name='Страна')  # нужно реализовать через выпадающий список
    nickname = models.CharField(max_length=30, verbose_name='Никнейм', help_text='Должен быть уникальным',
                                unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname


class Post(models.Model):
    rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=90, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    published_time = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    edited_time = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название рубрики', db_index=True)

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

    def __str__(self):
        return self.name
