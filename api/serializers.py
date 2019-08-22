from rest_framework import serializers

from shop_core.models import *

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = PropertyImage
		fields = ('image',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):

	images = ImageSerializer(many=True)

	url = serializers.URLField(source='get_absolute_url')

	class Meta:
	    model = Product
	    fields = (
	    	'id', 
	    	'in_sale',
	    	'is_new',
	    	'title', 
	    	'price',
	    	'sale_price',
	    	'specifications',
	    	'properties',
	    	'url', 
	    	'images', 
	    	)

class WhatBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('title', 'slug', )

class MenuSerializer(serializers.ModelSerializer):

	what_brand = WhatBrandSerializer(many=True)

	class Meta:
		model = Menu
		fields = (
			'title',
			'what_brand',
			'image',
			'slug',
			)

class CardItemSerializer(serializers.ModelSerializer):

	product = ProductSerializer()

	class Meta:
		model = CartItem
		fields = (
			'product',
			)

class CardSerializer(serializers.ModelSerializer):

	items = CardItemSerializer(many=True)

	class Meta:
		model = Card
		fields = (
			'items',
			)