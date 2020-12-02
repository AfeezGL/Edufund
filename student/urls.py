from django.urls import path, include
from .views import RegisterStudent, LoginStudent, CertificationView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'certifications', CertificationView, basename='certifications')

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterStudent.as_view(), name = 'student register'),
    path('login', LoginStudent.as_view(), name = 'student login')
]