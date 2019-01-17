from rest_framework.viewsets import ModelViewSet

from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer

class AtracaoViewset(ModelViewSet):
    serializer_class = AtracaoSerializer
    filter_fields = '__all__'

    def get_queryset(self):
        return Atracao.objects.all()