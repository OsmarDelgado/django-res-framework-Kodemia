from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import PetOwner, Pet, PetDate

"""PetOwner"""
class PetOwnersListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]

class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "address", "phone", "email"]

"""Pets"""
class PetsListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Pet
        fields = ["id", "name"]

class PetsModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "owner"]

"""PetDate"""
class PetDateListModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"]

class PetDateModelSerializer( serializers.ModelSerializer ):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type"]
