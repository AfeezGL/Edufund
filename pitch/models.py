from django.db import models
from account.models import User

class Pitch(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pitch')
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
