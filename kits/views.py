from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Kit
from .serializers import KitSerializer

# Create your views here.
class KitViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    API endpoint que permite visualizar os kits
    '''
    
    serializer_class = KitSerializer
    permission_classes = [permissions.AllowAny] # define acesso publico
    
    #* Queryset de busca de kits otimizado
    queryset = Kit.objects.all().prefetch_related( # prefetch_related busca todos os dados relacionados -> items do kit, produtos e categoria
        'kititem_set__product__category'
    )