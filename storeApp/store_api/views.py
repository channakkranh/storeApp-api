# from django.shortcuts import render
# from django.http import HttpResponse

# def test(request):
#     return HttpResponse('hello')
from django.shortcuts import render
from rest_framework import generics
from .models import Item,Location
from .serializers import ItemSerializers,LocationSerializer

class ItemList(generics.ListCreateAPIView):
    serializer_class=ItemSerializers

    def get_queryset(self):
        queryset=Item.objects.all()
        location=self.request.query_params.get(location)
        if location is not None:
            queryset=queryset.filter(itemlocation=location)
        return queryset
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ItemSerializers
    queryset=Item.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class=LocationSerializer
    queryset=Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=LocationSerializer
    queryset=Location.objects.all()

        