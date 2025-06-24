from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ManageUserView, AddressViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#* Criar Router para os endpoints baseados em ViewSet
router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    #* Rota para Registrar: POST /api/auth/register/
    path('register/', RegisterView.as_view(), name='auth_register'),

    #* Rota para Login: POST /api/auth/login/
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #* Rota para renovar o token de acesso: POST /api/auth/login/refresh/
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #* Rota para gerenciar o perfil do usuário logado: GET e PUT /api/auth/me/
    path('me/', ManageUserView.as_view(), name='manage_user'),
    
    #* Adiciona as URLs geradas pelo router (/address/, /address{id}/, ...) ao conjunto de URLs do site)
    path('', include(router.urls)),
]