from django.contrib import admin
from .models import Kit, KitItem

# Register your models here.
# O 'inline' permite adicionar/editar KitItems diretamente na página do Kit
class KitItemInline(admin.TabularInline):
    model = KitItem
    extra = 1 # Mostra um campo extra para adicionar um item por padrão
    
@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ('name', 'craft_type', 'difficulty', 'reference_month')
    inlines = [KitItemInline] # Adiciona o inline à página de admin do Kit