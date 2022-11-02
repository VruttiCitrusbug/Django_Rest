from . import models
from rest_framework import serializers
class serbook(serializers.ModelSerializer):
    class Meta:
        model = models.book
        fields= '__all__'
class serauther(serializers.ModelSerializer):
    class Meta:
        model = models.auther
        fields= '__all__'