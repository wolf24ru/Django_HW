from django.db import models


class Phone(models.Model):
    name = models.TextField('Имя', null=False)
    price = models.IntegerField('Цена')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    release_date = models.DateField('Дата релиза')
    lte_exists = ... #TODO узнать типа данных
    slug = models.SlugField()

