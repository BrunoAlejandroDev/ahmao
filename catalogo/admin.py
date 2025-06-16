'''
list_display: Controla as colunas exibidas na página de listagem.
list_filter: Cria uma barra lateral de filtros.
search_fields: Adiciona uma barra de pesquisa.
'''

from django.contrib import admin
from .models import Product, Category, CraftType, Difficulty

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #* Define quais colunas aparecerão na lista de produtos
    list_display = ('name', 'category', 'price')
    
    #* Adiciona uma barra lateral para filtrar produtos por categoria
    list_filter = ('category',)
    
    #* Adiciona um campo de busca que procura nos campos 'name' e 'description'
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

#* Modelos mais simples o registro básico 
admin.site.register(CraftType)
admin.site.register(Difficulty)