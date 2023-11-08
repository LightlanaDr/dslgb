# Generated by Django 4.2.7 on 2023-11-08 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(default=None, max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Эл. почта')),
                ('phone', models.CharField(default=None, max_length=12, verbose_name='Тел.')),
                ('address', models.CharField(default=None, max_length=250, verbose_name='Адрес')),
                ('data_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('data_update', models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')),
                ('status', models.CharField(choices=[('Неоплачен', 'Неоплачен'), ('Оплачен', 'Оплачен'), ('Доставляется', 'Доставляется'), ('Доставлен', 'Доставлен')], default='Неоплачен', max_length=100, verbose_name='Статус')),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Стоимость')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.neworder')),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Продукты в заказе',
            },
        ),
    ]
