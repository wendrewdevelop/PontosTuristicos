from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado = True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).partial_update(request, *args, **kwargs)

    #@action(methods = ['GET', 'POST'], detail = True)
    #def denunciar(self, request, pk = None):
    #    pass