from account.models import User
from .models import Certification
from knox.models import AuthToken
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .serializers import StudentSerializer, RegisterStudentSerializer, LoginStudentSerializer, CertificationSerializer

class RegisterStudent(generics.GenericAPIView):
    serializer_class = RegisterStudentSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": StudentSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginStudent(generics.GenericAPIView):
    serializer_class = LoginStudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": StudentSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class CertificationView(viewsets.ModelViewSet):
    serializer_class = CertificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.request.user.certs.all()
    
    def perform_create(self, serializer):
        serializer.save(student = self.request.user)