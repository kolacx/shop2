from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductSerializer, ImageSerializer, MenuSerializer, CardSerializer
from shop_core.models import *

# Create your views here.

class ProductV(APIView):

	def get(self, request):
		products = Product.objects.filter(is_active=True)
		serializer = ProductSerializer(products, many=True, context={'request': request})
		return Response({'data':serializer.data})


class MenuV(APIView):

	def get(self, request):
		menu = Menu.objects.all()
		serializer = MenuSerializer(menu, many=True)
		return Response({'data':serializer.data})


class CardV(APIView):

	def get(self, request):
		try:
			cart_id = request.session['cart_id']
			cart = Card.objects.get(id=cart_id)
		except:
			cart = Card()
			cart.save()
			cart_id = cart.id
			request.session['cart_id'] = cart_id
			cart = Card.objects.get(id=cart_id)

		serializer = CardSerializer(cart)
		return Response({'data' : serializer.data})