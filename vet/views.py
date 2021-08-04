from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics

# Serializers
from .serializers import PetDateListModelSerializer, PetDateModelSerializer, PetOwnerModelSerializer, PetOwnersListModelSerializer, PetsListModelSerializer, PetsModelSerializer

# Models
from .models import PetDate, PetOwner, Pet

"""Pet Owners"""
class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):
        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class

class PetOwnerRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer

"""Pets"""
class PetsListCreateAPIView( generics.ListCreateAPIView ):
    queryset = Pet.objects.all()
    serializer_class = PetsListModelSerializer

    def get_queryset( self ):
        name_filter = self.request.GET.get( "name" )
        filters = {}

        if name_filter:
            filters[ "name__icontains" ] = name_filter

        return self.queryset.filter( **filters )

    def get_serializer_class( self ):
        serializer_class = self.serializer_class

        if self.request.method == "POST":
            serializer_class = PetsModelSerializer

        return serializer_class

class PetsRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Pet.objects.all()
    serializer_class = PetsModelSerializer

"""PetDates"""
class PetDateListCreateAPIView( generics.ListCreateAPIView ):
    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset( self ):
        datetime_filter = self.request.GET.get( "datetime" )
        filters = {}

        if datetime_filter:
            filters[ "datetime__icontains" ] = datetime_filter

        return self.queryset.filter( **filters )

    def get_serializer_class( self ):
        serializer_class = self.serializer_class

        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer

        return serializer_class

class PetDateRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView ):
    queryset = PetDate.objects.all()
    serializer_class = PetDateModelSerializer
