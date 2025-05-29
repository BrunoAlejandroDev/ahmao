from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'descricao')
    list_filter = ('criado_em', 'atualizado_em')