from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='Картинка', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса ')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    preview = models.ImageField(upload_to='course/lesson', verbose_name='Картинка', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'