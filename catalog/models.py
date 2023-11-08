from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Category(models.Model):
    CHOICES_STATUS = (
        ('Опубликовано', 'Опубликовано'),
        ('Скрыто', 'Скрыто'),
    )

    name_cat = models.CharField(verbose_name='Категория', max_length=100)
    status = models.CharField(choices=CHOICES_STATUS, max_length=100, default='Опубликовано')

    def __str__(self):
        return f'{self.name_cat}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Фото', upload_to='products/')
    slug = models.SlugField(max_length=50, unique=True, default=title, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', default='')
    price = models.DecimalField(verbose_name='Стоимость',max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk, self.slug])
