from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    '''
        Nesse trecho eu deixo de receber somente os ID'S das atrações,
        para receber a atração por completo.
    '''
    atracoes = AtracaoSerializer(many = True)
    endereco = EnderecoSerializer()#não defini o 'many = True', pois a relação desse campo é unica
    comentarios = ComentarioSerializer(many = True)
    avaliacoes = AvaliacaoSerializer(many = True)

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = '__all__'

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)