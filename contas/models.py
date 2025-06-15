from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserRole(models.Model):
    name = models.TextField(unique=True)
    summary = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    #* Campos padrão do AbstractUser: username, first_name, last_name, email, password, etc.
    #* Campos customizados:
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=20)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True, related_name='users')
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address_name = models.TextField()
    street = models.TextField()
    number = models.TextField()
    complement = models.TextField(null=True, blank=True)
    neighborhood = models.TextField()
    city = models.TextField()
    state = models.TextField()
    postal_code = models.TextField(null=True, blank=True)
    country = models.TextField(default='Brasil')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.address_name} ({self.user.username})'