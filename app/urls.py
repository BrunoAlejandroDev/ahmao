"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="À mão - API",
      default_version='v1',
      description="API para o projeto À mão - um clube de assinatura de manualidades.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    
    #* Qualquer requisicao para /api/auth/... sera gerenciada pelo app 'contas'
    path('api/auth/', include('contas.urls')),
    path('api/catalogo/', include('catalogo.urls')), # Qualquer requisicao para api/catalogo/... sera gerenciada pelo app 'catalogo'

    # As linhas abaixo serão adicionadas no futuro, conforme desenvolvimento de cada funcionalidade
    # path('api/assinaturas/', include('assinaturas.urls')),
    # path('api/kits/', include('kits.urls')),
    # path('api/tutoriais/', include('tutoriais.urls')),

     # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
