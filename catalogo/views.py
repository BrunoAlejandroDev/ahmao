# catalogo/views.py
from rest_framework import viewsets, permissions
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet fornece automaticamente as ações `list`, `create`, `retrieve`,
    `update` e `destroy` para o modelo Produto.
    """
    queryset = Produto.objects.all().order_by('-criado_em') # Define o conjunto de objetos que este viewset irá operar.
    serializer_class = ProdutoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]