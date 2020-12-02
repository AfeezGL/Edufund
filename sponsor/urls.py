from django.urls import path
from .views import RegisterSponsor, LoginSponsor

urlpatterns = [
    path('register', RegisterSponsor.as_view(), name = 'sponsor register'),
    path('login', LoginSponsor.as_view(), name = 'sponsor login')
]