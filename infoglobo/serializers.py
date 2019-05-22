from .models import Item
from rest_framework_mongoengine import serializers


class ItemSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Item
        fields = '__all__'