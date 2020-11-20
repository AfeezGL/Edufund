from django.urls import path, include
from .views import Register, LoginApiView, GetUser
from knox import views as knox_views

urlpatterns = [
    path('api/knox/auth', include('knox.urls')),
    path('register', Register.as_view(), name = 'register'),
    path('login', LoginApiView.as_view(), name = 'login'),
    path('getuser', GetUser.as_view(), name = 'getuser'),
    path('logout', knox_views.LogoutView.as_view(), name = 'logout'),
]