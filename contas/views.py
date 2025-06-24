from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .models import User, Address, UserRole
from .serializers import RegisterSerializer, UserSerializer, AddressSerializer

User = get_user_model()

# View para o endpoint POST /api/auth/register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,) # permite que qualquer um se registre
    serializer_class = RegisterSerializer

# View para os endpoints GET e PUT /api/auth/me
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,) # exige que o usuário esteja logado

    def get_object(self):
        # Garante que o usuário só possa ver e editar seu próprio perfil
        return self.request.user
    
class AddressViewSet(viewsets.ModelViewSet):
    '''
    API endpoint que permite ao usuario registrar seus próprios endereços
    '''
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated] # exige que o usuario esteja logado
    
    def get_queryset(self):
        '''
        essa view deve retornar uma lista de endereços apenas para o usuario atualmente autenticado
        '''
        return self.request.user.addresses.all()
    
    def perform_create(self, serializer):
        '''
        Associa o endereço que esta sendo criado ao usuario que está fazendo a requisicao
        '''
        serializer.save(user=self.request.user)