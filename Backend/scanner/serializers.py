from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Scan

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

class ScanSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Scan
        fields = ('file_name','image','date_created')

        