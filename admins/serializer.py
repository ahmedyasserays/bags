from rest_framework import serializers
from .models import ID_name

class idnameSerializer(serializers.ModelSerializer):
  class Meta:
    model =  ID_name
    fields = ['id_key','name']