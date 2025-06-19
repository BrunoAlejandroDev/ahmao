
#* Importacoes Gerais
from rest_framework import serializers

#* Importacoes de arquivos
from .models import Kit, KitItem
from catalogo.serializers import ProductSerializer 

class KitItemSerializer(serializers.ModelSerializer):
    """
    Serializer para o item do kit. Ele mostra os detalhes do produto e a quantidade.
    """
    
    product = ProductSerializer(read_only = True) # mostrar os detalhes dos produtos do kit ao inves de apenas o ID
    
    class Meta:
        model = KitItem
        fields = ['quantity', 'product']
        
class KitSerializer(serializers.ModelSerializer):
    """
    Serializer principal para o Kit.
    """
    
    #* Mostrar os nomes dos campos de craft type e difficulty
    craft_type = serializers.StringRelatedField()
    difficulty = serializers.StringRelatedField()
    
    #* Campo de itens do kit
    items = KitItemSerializer(source='kititem_set', many=True, read_only=True)
    
    class Meta:
        model = Kit
        fields = [
            'id',
            'name',
            'description',
            'reference_month',
            'craft_type',
            'difficulty',
            'items' # campo de lista de produtos
        ]