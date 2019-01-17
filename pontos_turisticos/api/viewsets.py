from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado = True)