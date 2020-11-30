from django.urls import path
from .views import RegisterStudent, LoginStudent

urlpatterns = [
    path('register', RegisterStudent.as_view(), name = 'student register'),
    path('login', LoginStudent.as_view(), name = 'student login')
]