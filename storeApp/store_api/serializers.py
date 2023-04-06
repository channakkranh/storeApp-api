from rest_framework import serializers
from .models import Item,Location

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('__all__')

class LocationSerializer(serializers.ManyRelatedField):
    class Meta:
        model=Location
        field=('__all__')
        