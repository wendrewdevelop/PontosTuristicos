from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer

class EnderecoViewset(ModelViewSet):
    serializer_class = EnderecoSerializer
    filter_fields = '__all__'

    def get_queryset(self):
        return Endereco.objects.all()