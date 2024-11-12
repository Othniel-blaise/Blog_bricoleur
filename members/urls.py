 
from django.urls import path
from .views import UserRegisterView
urlpatterns = [
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),  # L'URL pour la page de création de compte
]
