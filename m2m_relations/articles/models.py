from django.db import models


class Tag(models.Model):
    # article = models.ManyToManyField(Article, through='ArticleTag', related_name='tags')
    name = models.TextField('Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField(Tag, through='ArticleTag', related_name='article')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, related_name='t_tag', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='t_article', on_delete=models.CASCADE)
    is_main = models.BooleanField()
    # TODO добавить уникальности is_main

    class Meta:
        verbose_name = 'Тег к статьи'
        verbose_name_plural = 'Теги к статьи'
        ordering = ['-is_main', 'tag']
