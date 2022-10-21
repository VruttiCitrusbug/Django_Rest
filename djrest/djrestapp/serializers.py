
from rest_framework import serializers
from . import models

class stuser(serializers.ModelSerializer):
    class Meta:
        model=models.student
        fields=(
            'name','age'
        )