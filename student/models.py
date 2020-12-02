from django.db import models
from account.models import User


class Certification(models.Model):
    student = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "certs")
    title = models.CharField(max_length = 100)
    result = models.FileField()

    def __str__(self):
        return f"{self.title} {self.student.email}"
