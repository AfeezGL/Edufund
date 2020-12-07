from .views import PitchView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PitchView)


urlpatterns = [
    path('', include(router.urls))
]