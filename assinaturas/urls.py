
#* Importacoes
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'subscription', views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('plans/', views.PlanListView.as_view(), name='plan-list'), #* a URL sera /api/assinaturas/plans
    path('', include(router.urls)), #* adiciona as urls geradas pelo router para o CRUD de assinaturas
]