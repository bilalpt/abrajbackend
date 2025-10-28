from rest_framework import serializers
from .models import Roombooking

class RoombookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roombooking
        fields = '__all__'
