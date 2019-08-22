from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductV.as_view()),
    path('menu/', MenuV.as_view()),
    path('card/', CardV.as_view()),
]
