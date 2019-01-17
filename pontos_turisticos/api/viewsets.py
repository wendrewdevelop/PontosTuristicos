from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer