# catalogo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

# Cria uma instância do DefaultRouter.
# DefaultRouter também cria automaticamente uma view raiz da API (API Root) que lista todos os endpoints registrados.
router = DefaultRouter()

# Registra o ProdutoViewSet com o router.
# 'produtos' será o prefixo da URL para os endpoints relacionados a Produto.
# Ex: /api/catalogo/produtos/ e /api/catalogo/produtos/<pk>/
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)), # Inclui as URLs geradas pelo router.
]