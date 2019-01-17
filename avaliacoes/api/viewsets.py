from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacaoSerializer

class AvaliacaoViewset(ModelViewSet):
    serializer_class = AvaliacaoSerializer
    filter_fields = '__all__'

    def get_queryset(self):
        return Avaliacao.objects.all()