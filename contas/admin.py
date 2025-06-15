from django.contrib import admin
from .models import User, UserRole, Address

# Registra os modelos para que apareçam na interface de administração
admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(Address)