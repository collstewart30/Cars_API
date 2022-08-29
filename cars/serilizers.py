from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price', 'dealership']
        depth = 1

    dealership_id = serializers.IntegerField(write_only=True)