from django.db import models

from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

class PontoTuristico(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default = False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ManyToManyField(Endereco)

    def __str__(self):
        return self.nome
