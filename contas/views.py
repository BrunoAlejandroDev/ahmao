from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer

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