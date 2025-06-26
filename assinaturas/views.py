
#* Importacoes
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import Plan, Subscription
from .serializers import PlanSerializer, SubscriptionSerializer


'''
API endpoint que lista todos os planos de assinatura ativos
'''
class PlanListView(generics.ListAPIView): #* apenas lista dados 
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny] #* rota publica
    
    def get_queryset(self):
        #* retornar apenas os planos que estao ativos
        return Plan.objects.filter(is_activate = True)
    
class SubscriptionViewSet(viewsets.ModelViewSet):
    '''
    API endpoint que permite aos usuarios gerenciarem suas proprias assinaturas
    '''
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated] # necessario login
    
    #* queryset para retornar apenas as assinaturas do usuario que esta fazendo a requisiçao
    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user) 
    
    #* associoa a nova assinatura ao usuario logado no momento da requisicao
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)