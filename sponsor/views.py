from account.models import User
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import SponsorSerializer, RegisterSponsorSerializer, LoginSponsorSerializer

class RegisterSponsor(generics.GenericAPIView):
    serializer_class = RegisterSponsorSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": SponsorSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginSponsor(generics.GenericAPIView):
    serializer_class = LoginSponsorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": SponsorSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })