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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #* Qualquer requisicao para /api/auth/... sera gerenciada pelo app 'contas'
    path('api/auth/', include('contas.urls')),

    # As linhas abaixo serão adicionadas no futuro, conforme desenvolvimento de cada funcionalidade
    # path('api/catalogo/', include('catalogo.urls')), # Qualquer requisicao para api/catalogo/... sera gerenciada pelo app 'catalogo'
    # path('api/assinaturas/', include('assinaturas.urls')),
    # path('api/kits/', include('kits.urls')),
    # path('api/tutoriais/', include('tutoriais.urls')),
]
