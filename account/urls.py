from django.urls import path
from rest_framework.authtoken import views as rest_views
from .views import Register

urlpatterns = [
    path('auth-token/', rest_views.obtain_auth_token),
    path('register/', Register.as_view(), name = 'register'),
]