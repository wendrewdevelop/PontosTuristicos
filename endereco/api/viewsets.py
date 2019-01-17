from rest_framework.viewsets import ModelViewSet

from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer

class EnderecoViewset(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer