from rest_framework import serializers
from .models import Pitch
from account.models import User

class PitchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pitch
        fields = ['id', 'text', 'created_at', 'updated_at', 'student']
        depth = 1

class PitchWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitch
        fields = ['id', 'text']