# catalogo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Cria uma instância do DefaultRouter.
# DefaultRouter também cria automaticamente uma view raiz da API (API Root) que lista todos os endpoints registrados.
router = DefaultRouter()

# Registra o ProductViewSet com o router. 'products' será o prefixo da URL para os endpoints relacionados a Produto.
# Ex: /api/catalogo/products/ e /api/catalogo/products/<pk>/ (detalhe)
router.register(r'products', views.ProdutoViewSet, basename='product')

#* Definir as rotas para as views de lista, de forma a associar cada path com uma view
urlpatterns = [ 
    path('', include(router.urls)), # Inclui as URLs geradas pelo router.
    
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('craft-types/', views.CraftTyperListView.as_view(), name='craft-type-list'),
    path('difficulties/', views.DifficultyListView.as_view(), name='difficulty-list')
]