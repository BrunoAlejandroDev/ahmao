'''
CategorySerializer, CraftTypeSerializer, DifficultySerializer são serializers (tradutores) dos dados do banco para formato JSON. Herdam de ModelSerializer
'''

# catalogo/serializers.py
from rest_framework import serializers
from .models import Product, Category, CraftType, Difficulty

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
class CraftTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CraftType
        fields = ['id', 'name']
        
class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['id', 'name']
        
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() # serve para mostrar o nome da categoria ao inves de apenas o ID
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'url_image', 
            'category'
        ]