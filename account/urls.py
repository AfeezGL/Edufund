from django.urls import path, include
from .views import Register, LoginApiView, GetUser
from knox import views as knox_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/knox/auth', include('knox.urls')),
    path('register', Register.as_view(), name = 'register'),
    path('login', LoginApiView.as_view(), name = 'login'),
    path('getuser', GetUser.as_view(), name = 'getuser'),
    path('logout', knox_views.LogoutView.as_view(), name = 'logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)