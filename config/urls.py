"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from pontos_turisticos.api.viewsets import PontoTuristicoViewset
from atracoes.api.viewsets import AtracaoViewset
from endereco.api.viewsets import EnderecoViewset
from comentarios.api.viewsets import ComentarioViewset
from avaliacoes.api.viewsets import AvaliacaoViewset

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewset, base_name = 'PontoTuristico')
router.register(r'atracoes', AtracaoViewset, base_name = 'Atracao')
router.register(r'endereco', EnderecoViewset, base_name = 'Endereco')
router.register(r'comentarios', ComentarioViewset, base_name = 'Comentario')
router.register(r'avaliacoes', AvaliacaoViewset, base_name = 'Avaliacao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
