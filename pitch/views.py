from .serializers import PitchSerializer, PitchWriteSerializer
from rest_framework import viewsets, permissions
from .models import Pitch
from account.permissions import IsStudentOrReadOnly
from rest_framework.permissions import SAFE_METHODS


class PitchView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStudentOrReadOnly]
    queryset = Pitch.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in SAFE_METHODS:
            return PitchSerializer
        return PitchWriteSerializer

    def perform_create(self, serializer):
        serializer.save(student = self.request.user)