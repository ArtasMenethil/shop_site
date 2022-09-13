from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    slug = models.SlugField('Уникальное название курса')   # аналог id, но позволяет использовать строки вместо
    # чисел
    title = models.CharField('Заголовок', max_length=120)
    description = models.TextField('Описание курса')
    image = models.ImageField('Изображение', default='default.jpg', upload_to='course_img')
    is_free = models.BooleanField('Бесплатно?', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'


class Lesson(models.Model):
    # slug, title, description, course, number, video_url
    slug = models.SlugField('Уникальное название урока')  # аналог id, но позволяет использовать строки вместо чисел
    title = models.CharField('Заголовок урока', max_length=120)
    description = models.TextField('Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField('Номер урока')
    video = models.CharField('URL видео', max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'


class Comments(models.Model):
    comment = models.TextField('Напишите комментарий')
    author_com = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_com = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={'comm': self.lesson_com.comment})

