from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.urls import reverse

from .models import *

class Product(models.Model):
	is_active = models.BooleanField(default=True, verbose_name='Доступный товар?')
	in_sale = models.BooleanField(default=False, verbose_name='Учавствует в распродаже?')
	is_new = models.BooleanField(default=False, verbose_name='Новый товар?')
	title = models.CharField(max_length=200, verbose_name='Заголовок')

	price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
	sale_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена с Скидкой', blank=True, default=0.00)

	menu = models.ForeignKey('Menu', verbose_name='К какой категории?', on_delete=models.CASCADE, blank=True, null=True)
	category = models.ForeignKey('Category', verbose_name='Бренд', on_delete=models.CASCADE, blank=True, null=True)
	model_phone = models.ForeignKey('ModelPhone', verbose_name='Модель', on_delete=models.CASCADE, blank=True, null=True)

	specifications = RichTextField(verbose_name='Характеристики', blank=True)
	properties = RichTextField(verbose_name='Свойства', blank=True)

	create_date = models.DateTimeField(auto_now_add=True, null=True)

	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.title
	   	
	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"

	def get_absolute_url(self):
		return reverse('product_url', kwargs={'product':self.slug})

def image_folder(instance, filename):
	filename = instance.slug + '.' + filename.split('.')[1]
	return "{0}/{1}".format(instance.slug, filename)

class PropertyImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')


class Menu(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название категории')
	what_brand = models.ManyToManyField('Category', verbose_name="Какие категории сюда входят?", blank=True)
	image = models.ImageField(upload_to='products', null=True)

	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)


	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"


	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название бренда')
	phone_models = models.ManyToManyField('ModelPhone', verbose_name="Какие модели сюда входят?")
	image = models.ImageField(upload_to='products', null=True)

	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.title
	   	
	class Meta:
		verbose_name = "Бренд"
		verbose_name_plural = "Бренды"


class ModelPhone(models.Model):
	title = models.CharField(max_length=100, verbose_name="Модель телефона")
	slug = AutoSlugField(populate_from='title', unique=True, db_index=True, editable=True, blank=True)

	def __str__(self):
		return self.title
	   	
	class Meta:
		verbose_name = "Модель"
		verbose_name_plural = "Модели"


class CartItem(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	item_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

	def __str__(self):
		return self.product.title


class Card(models.Model):

	items = models.ManyToManyField(CartItem, blank=True)

	def __str__(self):
		return str(self.id)