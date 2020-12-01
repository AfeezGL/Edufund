from django.shortcuts import render
from .models import User
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user