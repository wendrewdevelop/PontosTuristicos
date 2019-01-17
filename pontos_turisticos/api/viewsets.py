from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        #Definindo parametros de busca
        '''
            O paramêtro poderia ser definido como uma lista, porém
            se não fosse preenchido o sistema apresentaria um erro.

            id = self.request.query_params['id']
        '''
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        
        #Instanciando a queryset
        queryset = PontoTuristico.objects.all()
        
        if id:#se o ID existir
            queryset.filter(id = id)#busca ID

        if nome:#se o NOME existir
            queryset.filter(nome__iexact = nome)#busca NOME

        if descricao:#se DESCRICAO existir
            queryset.filter(descricao__iexact = descricao)#busca DESCRICAO

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewset, self).list(request, *args, **kwargs)

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

    @action(methods = ['GET', 'POST'], detail = True)
    def denunciar(self, request, pk = None):
        pass