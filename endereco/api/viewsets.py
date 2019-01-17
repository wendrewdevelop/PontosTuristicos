from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer

class EnderecoViewset(ModelViewSet):
    serializer_class = EnderecoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('linha1', 'cidade', 'estado', 'pais')

    def get_queryset(self):
        return Endereco.objects.all()