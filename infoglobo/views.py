from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework_mongoengine import viewsets as meviewsets


class ItemList(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Item.objects.all()
    serializer_class = ItemSerializer