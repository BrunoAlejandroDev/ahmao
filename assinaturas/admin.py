
#* Importacoes
from django.contrib import admin
from .models import Plan, Subscription

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'frequency', 'is_activate')
    list_filter = ('is_activate',)
    search_fields = ('name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'status', 'start_date')
    list_filter = ('status', 'plan',)
    search_fields = ('user__username', 'plan__name',)