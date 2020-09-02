from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    favorite = models.BooleanField(default=False, verbose_name='Основной')
    article = models.ManyToManyField(Article, verbose_name='Статьи', related_name='tags', blank=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ["name"]

    def __str__(self):
        return self.name