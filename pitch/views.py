from .serializers import PitchSerializer
from rest_framework import viewsets, permissions
from .models import Pitch
from account.permissions import IsStudentOrReadOnly


class PitchView(viewsets.ModelViewSet):
    serializer_class = PitchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStudentOrReadOnly]
    queryset = Pitch.objects.all()

    def perform_create(self, serializer):
        serializer.save(student = self.request.user)