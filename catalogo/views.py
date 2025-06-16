'''
queryset -> define o conjunto de dados que a view irá operar 
permission_classes = [permissions.AllowAny] -> define essas rotas como publicas, qualquer pessoa pode acessá-las
'''

# catalogo/views.py
from rest_framework import viewsets, permissions, generics
from .models import Product, Category, CraftType, Difficulty
from .serializers import (ProductSerializer, CategorySerializer, CraftTypeSerializer, DifficultySerializer)

#* O ViewSet para Produtos combina a lógica de listar todos os produtos e detalhar um produto em uma única classe.
class ProdutoViewSet(viewsets.ReadOnlyModelViewSet): # ReadOnly pois permite apenas operacoes de leitura (GET)
    """
    API endpoint que permite visualizar produtos.
    Fornece as ações `list` (GET /products) e `retrieve` (GET /products/{id}).
    """
    queryset = Product.objects.all() # Define o conjunto de objetos que este viewset irá operar.
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny] # permitir acesso publico
    
class CategoryListView(generics.ListAPIView):
    #* API endpoint para listar todas as categorias.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
class CraftTyperListView(generics.ListAPIView):
    #* API endpoint para listar todos os tipos de manualidade
    queryset = CraftType.objects.all()
    serializer_class = CraftTypeSerializer
    permission_classes = [permissions.AllowAny]
    
class DifficultyListView(generics.ListAPIView):
    #* API endpoint para listar todos os níveis de dificuldade. 
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes = [permissions.AllowAny]