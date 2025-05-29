# catalogo/serializers.py
from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    # Ele cria automaticamente campos baseados no modelo e validadores.
    class Meta:
        model = Produto  # Especifica o modelo que este serializer irá manipular
        fields = ['id', 'nome', 'descricao', 'valor', 'criado_em', 'atualizado_em']
        read_only_fields = ['criado_em', 'atualizado_em']
        # Campos que devem ser lidos da API, mas não devem ser definidos diretamente ao criar/atualizar.