# Generated by Django 2.2 on 2019-04-30 08:00

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название бренда')),
                ('image', models.ImageField(null=True, upload_to='products')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='ModelPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Модель телефона')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('image', models.ImageField(null=True, upload_to='products')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True)),
                ('what_brand', models.ManyToManyField(blank=True, to='shop_core.Category', verbose_name='Какие категории сюда входят?')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='phone_models',
            field=models.ManyToManyField(to='shop_core.ModelPhone', verbose_name='Какие модели сюда входят?'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_core.Category', verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='product',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_core.Menu', verbose_name='К какой категории?'),
        ),
        migrations.AddField(
            model_name='product',
            name='model_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_core.ModelPhone', verbose_name='Модель'),
        ),
    ]