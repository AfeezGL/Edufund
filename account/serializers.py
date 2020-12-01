from rest_framework import serializers
from .models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for handling profile updates
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'profile_picture', 'phone_number']