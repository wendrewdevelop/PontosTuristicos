from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer

class AtracaoViewset(ModelViewSet):
    serializer_class = AtracaoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'descricao')
    

    def get_queryset(self):
        return Atracao.objects.all()