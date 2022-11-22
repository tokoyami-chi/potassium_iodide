from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Назва категорії', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія блогу'
        verbose_name_plural = 'Категорії блогу'


class Tag(models.Model):
    name = models.CharField(verbose_name='Тег', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Категорія', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Назва', max_length=255)
    text_preview = models.TextField(verbose_name='Превью тексту', null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публікації')
    updatet_at = models.DateTimeField(verbose_name='Дата зміни', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
