
from dataclasses import field, fields
import imp
from pyexpat import model
from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
class stuser(serializers.ModelSerializer):
    class Meta:
        model=models.student
        fields=(
            'name','age'
        )
class seruser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']