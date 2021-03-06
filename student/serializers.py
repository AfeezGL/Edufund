from rest_framework import serializers
from account.models import User
from .models import Certification
from django.contrib.auth import authenticate


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the user model
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_student']


class RegisterStudentSerializer(serializers.ModelSerializer):
    """
    User serializer for the Student registration view
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_student = True
        user.save()
        return user


# Login serializer
class LoginStudentSerializer(serializers.Serializer):
    """
    User serializer for the Student login view
    """
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")


class CertificationSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Certification model
    """
    class Meta:
        model = Certification
        fields = ['id', 'title', 'result']
        read_only_fields = ['student']
