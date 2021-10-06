from django.db import models
from django.urls import reverse


# Create your models here.


class News(models.Model):
    # blank=True - поле не обязательно
    # null=True - можно сделать зависимость при наличии элементов в бд без конфликта
    title = models.CharField(max_length=60, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'                     # название в админке
        verbose_name_plural = 'Новости'              # можественное название в админке
        ordering = ['-created_at', 'title']          # сортировка порядка новостей в админке, "-" обратный порядок


class Category(models.Model):
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'                   # название в админке
        verbose_name_plural = 'Категории'            # можественное название в админке
        ordering = ['title']
