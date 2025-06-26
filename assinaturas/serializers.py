
#* Importacoes
from rest_framework import serializers
from .models import Plan, Subscription

class PlanSerializer(serializers.ModelSerializer):
    '''
    serializer para listar os planos de assinatura disponiveis
    '''
    class Meta:
        model = Plan
        fields = [
            'id',
            'name',
            'description',
            'price',
            'frequency'
        ]
        
class SubscriptionSerializer(serializers.ModelSerializer):
    '''
    serializer para criar e visualizar as assinaturas do usuario
    '''
    #* leitura (get) para mostrar o nome do plano
    plan = serializers.StringRelatedField(read_only=True)
    difficulty = serializers.StringRelatedField(read_only=True)
    craft_type = serializers.StringRelatedField(read_only=True)
    
    #* escrita (post): campos que o front-end enviara
    plan_id = serializers.IntegerField(write_only=True) #* garante que os campos só sejam usados para criar/atualizar
    difficulty_id = serializers.IntegerField(write_only=True)
    craft_type_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Subscription
        fields = [
            'id',
            'user',
            'plan',             # Campo de leitura (nome)
            'plan_id',          # Campo de escrita (ID)
            'start_date',
            'status',
            'difficulty',       # Campo de leitura (nome)
            'difficulty_id',    # Campo de escrita (ID)
            'craft_type',       # Campo de leitura (nome)
            'craft_type_id',    # Campo de escrita (ID)
        ]
        read_only_fields = ['user', 'start_date']