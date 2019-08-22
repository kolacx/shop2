# Generated by Django 2.2 on 2019-04-17 11:03

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступный товар?')),
                ('in_sale', models.BooleanField(default=False, verbose_name='Учавствует в распродаже?')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новый товар?')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, verbose_name='Цена с Скидкой')),
                ('specifications', ckeditor.fields.RichTextField(blank=True, verbose_name='Характеристики')),
                ('properties', ckeditor.fields.RichTextField(blank=True, verbose_name='Свойства')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop_core.Product')),
            ],
        ),
    ]
