from django.db import models
from django.template.defaultfilters import slugify


class Image(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
