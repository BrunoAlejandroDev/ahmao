from rest_framework import serializers
from .models import User, Address, UserRole

#* Serializer para Registrar um novo usuário
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'cpf', 'phone') # campos para o registro

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            cpf=validated_data['cpf'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

#* Serializer para Visualizar e Atualizar dados do usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'cpf', 'phone', 'role') # campos para o registro
        read_only_fields = ('username', 'role')
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'user', 
            'address_name',
            'street',
            'number',
            'complement',
            'neighborhood',
            'city',
            'state',
            'postal_code',
            'country',
            'created_at'
        ]
        read_only_fields = ['user'] # campo para garantir que o usuario sera definido pela logica da view 
        
'''
read_only_fields = ['user']: impede que um usuario tente criar um endereço para outra pessoa. O campo user nunca deve ser aceito como dado de entrada
'''